from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.backends import ModelBackend
from django.forms import ModelForm, CharField, PasswordInput
from django.contrib.auth.models import User


class UsuarioForm(ModelForm):
    password = CharField(max_length=32, widget=PasswordInput)

    def save(self, commit=True):
        user = super(UsuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UsuarioEditForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
