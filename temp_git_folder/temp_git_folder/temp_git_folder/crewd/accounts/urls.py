from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('role-selection/', views.RoleSelectionView.as_view(), name='role_selection'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.logout_view, name='logout'),
]