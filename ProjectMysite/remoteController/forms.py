from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# extende o Form do Django e adiciona ao formolario o campo de Email

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)  # não gravo já
        user.email = self.cleaned_data['email']  # primeiro modifico
        if commit:
            user.save()  # e agora sim gravo
        return user


