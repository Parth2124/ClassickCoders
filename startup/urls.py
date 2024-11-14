from django.urls import path
from myproject import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns =  [
    path('', views.index ,name = 'index' ),
    path('contact/', views.contact_view, name='contact'),
    path('sem1_Y1/', views.sem1_view, name='sem1_Y1'),
    path('sem2_Y1/', views.sem2_view, name='sem2_Y1'),
    path('sem3_Y2/', views.sem3_view, name='sem3_Y2'),
    path('sem4_Y2/', views.sem4_view, name='sem4_Y2'),
    path('sem5_Y3/', views.sem5_view, name='sem5_Y3'),
    path('sem6_Y3/', views.sem6_view, name='sem6_Y3'),
    path("register/",views.register, name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),

     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
]
