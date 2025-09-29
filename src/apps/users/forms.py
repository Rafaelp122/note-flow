from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)

from apps.core.forms import FormStylingMixin
from apps.core.utils.django_forms import add_placeholder

from .models import User


class CustomUserCreationForm(FormStylingMixin, UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['username'], 'Your username')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password1'], 'Type your password here')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1')

    username = forms.CharField(
        help_text=(
            "Username can contain letters, numbers, and @/./+/-/_ characters. "
            "The length should be between 4 and 30 characters."
        ),
        error_messages={
            'min_length': 'Username must have at least 4 characters',
            'max_length': 'Username must have less than 150 characters'
        },
        min_length=4,
        max_length=30,
    )
    first_name = forms.CharField(
        required=False,
        help_text="Optional",
    )
    last_name = forms.CharField(
        required=False,
        help_text="Optional",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(),
        label=("Password"),
        help_text=(
            "Password must be at least 8 characters, not entirely numeric, "
            "and not too common or similar to your personal information."
        ),
    )


class SignInForm(FormStylingMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['username'], 'Enter your username')
        add_placeholder(self.fields['password'], 'Enter your password')


class CustomUserChangeForm(FormStylingMixin, UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
