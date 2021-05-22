from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # TODO: should be replaced, when home view is ready
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
