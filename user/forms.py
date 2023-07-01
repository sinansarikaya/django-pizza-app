from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):

    extra_field = forms.CharField(max_length=128, required=False)

    class Meta(UserCreationForm.Meta):
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'extra_field',
            'password',
            'password2',
        )