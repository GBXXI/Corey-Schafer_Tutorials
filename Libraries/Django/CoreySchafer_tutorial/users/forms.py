# We create a custom form by inheriting from the django.form class.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Adds the email field to our form.

    class Meta:  # In this class, we specify the model that we want our form to
        # interact with. So, whenever this form validates it's creating
        # a new user.
        # This class gives us a namespace for configurations and keeps
        # them in one place.
        model = User
        fields = [  # These are the fields - and their order- that are going to
                    # be shown in our form.
            'username',
            'email',
            'password1',
            'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
