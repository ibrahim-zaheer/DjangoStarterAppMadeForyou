#use this code when want to set staff status for user to true


# # forms.py
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Optionally, you can customize the labels, placeholders, etc.

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_staff = True  # Set is_staff to True
#         if commit:
#             user.save()
#         return user


#use this code when want to set staff status for user to true and assign it to a certain group
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    group_name = "marketing"  # Name of the group to which the user will be assigned

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally, you can customize the labels, placeholders, etc.

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Set is_staff to True
        if commit:
            user.save()
            group = Group.objects.get(name=self.group_name)
            user.groups.add(group)  # Add user to the group
        return user
