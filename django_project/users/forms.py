from django import forms
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Comment
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email', 'password1', 'password2']


# class UserRegisterForm(forms.ModelForm):
#     password1 = forms.CharField(label = 'password' , widget= forms.PasswordInput)
#     password2 = forms.CharField(label = 'confirm password' , widget= forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ("email",'password1','password2',)

#     def clean_password2(self):
#         # Check if the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords do not match")
#         return password2
#     def save(self):
#         user = super(UserRegisterForm, self).save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         user.save()
#         return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }