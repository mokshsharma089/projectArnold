from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Mandatory')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    birth_date=forms.DateField(required=False)
    bio=forms.CharField(widget=forms.Textarea,required=False)
    location=forms.CharField(max_length=256,required=False)
    class Meta:
        model = Profile
        fields = ('birth_date', 'bio', 'location')

class UserForm(forms.ModelForm):
    class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email')