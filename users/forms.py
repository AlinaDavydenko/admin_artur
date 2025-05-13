from catalog.forms import StyleFormMixin

from message.models import User

from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")
