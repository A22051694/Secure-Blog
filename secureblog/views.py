from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comment
from django.contrib import messages
from django.views import View
from django.shortcuts import render

#  List published posts
class PostListView(ListView):
    model = Post
    template_name = 'secureblog/post_list.html'
    context_object_name = 'object_list'  # Fix for template compatibility
    queryset = Post.objects.filter(is_published=True) # select * from post where is_published = True

#  View post detail
class PostDetailView(DetailView):
    model = Post
    template_name = 'secureblog/post_detail.html'
    context_object_name = 'object'  # Fix for template compatibility

#  Create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'is_published']
    template_name = 'secureblog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

#  Update a post (only the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'is_published']
    template_name = 'secureblog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return UpdateView.form_valid(self, form)

    def test_func(self):
        return self.get_object().author == self.request.user

#  Delete a post (only the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'secureblog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        # Ensure only the author can delete the post.
        return self.get_object().author == self.request.user


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk, is_published=True)
        Comment.objects.create(
            author=request.user,
            body=request.POST.get('body'),
            post=post
        )
        return redirect('post_detail', pk=pk)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, is_published=True)
        return render(request, 'secureblog/comment_form.html', {'post': post})

# Delete a comment (only the author)
class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'secureblog/comment_confirm_delete.html'
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        # Assuming the post detail URL follows the pattern "/post/<post_pk>/ POST/2
        return '/post/' + str(self.object.post.pk) + '/'
    
    def delete(self, request):
        messages.success(request, 'Comment deleted successfully.')
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())
