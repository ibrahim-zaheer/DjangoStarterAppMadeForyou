from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
# #if not want to use forms.py and just this code and register.html for making users then this is enough

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(request, user)  # Call send_verification_email with the user object
            # return redirect('verification_sent')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

#now make this code when you want to redirect the user after login
def home(request):
    return render(request,"home.html")
# these are code for password reset related things in django
# views.py



class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = '/password-reset/done/'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/login/'

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

#for handling emails:
# views.py



def send_verification_email(request, user):
    token_generator = default_token_generator
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': uid,
        'token': token,
    })
    user.email_user(mail_subject, message)
    return redirect('verification_sent')

def verify_email(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_encode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('verification_success')
    else:
        return redirect('verification_fail')
    
def verification_success(request):
    return render(request, 'verification_success.html')

def verification_fail(request):
    return render(request, 'verification_fail.html')    
    


# #if want to use forms.py and set some default functions like staff status on and so on then use this:
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})


#if want to use forms.py and set some default functions like staff status on and also set it to a certain group and so on then use this:
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})
