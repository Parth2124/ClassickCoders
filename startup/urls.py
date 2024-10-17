from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =  [
    path('', views.index ,name = 'index' ),
    path('contact/', views.contact_view, name='contact'),
    path("register/",views.register, name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),

     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
]