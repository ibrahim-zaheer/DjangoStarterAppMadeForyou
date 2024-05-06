# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# #if not want to use forms.py and just this code and register.html for making users then this is enough
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
            
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

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
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
