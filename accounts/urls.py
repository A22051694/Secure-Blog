from django.urls import path
from accounts.views import RegisterView, UserLoginView, UserLogoutView, DashboardView

urlpatterns = [
    # Define your URL patterns here
    # Example: path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),  # This is correct
    path('profile/', DashboardView.as_view(), name='dashboard'),
]