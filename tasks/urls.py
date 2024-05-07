from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('home/', views.home, name='home'),

     #for password related things

      path('password-reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    #for handling emails:
     path('send-verification-email/', views.send_verification_email, name='send_verification_email'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify_email'),
    path('verification-success/', views.verification_success, name='verification_success'),
    path('verification-fail/', views.verification_fail, name='verification_fail'),
]