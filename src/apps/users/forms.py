from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            attrs = field.widget.attrs
            # Get current classes, split into list
            classes = attrs.get('class', '').split()

            # Add form-control if not already present
            if 'form-control' not in classes:
                classes.append('form-control')

            # Add is-invalid if the field has errors
            if field_name in self.errors and 'is-invalid' not in classes:
                classes.append('is-invalid')

            # Join classes back into a string
            attrs['class'] = ' '.join(classes)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
