from django.urls import path
from . import views

urlpatterns = [
    # User
    path('register/', views.register, name ='register'),
    path('validate_register/', views.validate_register, name = 'validate_register'),
    path('login/', views.login, name ='login'),
    path('validate_login/', views.validate_login, name = 'validate_login'),
    path('logout/', views.logout, name = 'logout'),

    # Store
    path('', views.home, name = 'home'),
    path('create_store/', views.create_store, name = 'create_store'),
    path('my_store/', views.my_store, name = 'my_store'),
    path('store/<int:id>', views.store, name = 'store'),
]
