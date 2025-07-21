from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from secureblog.models import Post, Comment

# Register View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'  
    success_url = reverse_lazy('login')

# Login View (uses built-in template)
class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  

# Logout View (no template needed)
class UserLogoutView(LogoutView):
    next_page = 'post_list'  # Redirect to post list after logout
    http_method_names = ['get', 'post']  # Allow GET requests for logout

# Dashboard View (only accessible when logged in)
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'  # Fix path
    login_url = reverse_lazy('login')  # Redirect to login if not authenticated
    def get_context_data(self, **_):
        return {
            'user_posts': Post.objects.filter(author=self.request.user),
            # SELECT * FROM post WHERE author_id = <current_user_id>;
            'user_comments': Comment.objects.filter(author=self.request.user),
            # SELECT * FROM comment WHERE author_id = <current_user_id>;
        }


# User's Posts View
class UserPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'accounts/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user) # SELECT * FROM post WHERE author_id = <current_user_id>;
    

# User's Comments View  
class UserCommentsView(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'accounts/user_comments.html'
    context_object_name = 'comments'
    paginate_by = 20
    
    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user) # SELECT * FROM comment WHERE author_id = <current_user_id>;
