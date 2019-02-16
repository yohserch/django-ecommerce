from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    fullname = forms.CharField(
        widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your full name"
                }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your Email"
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Your content"
            }
        )
    )


class LoginForm(forms.Form):
    """LoginForm definition."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    """RegisterForm definition."""

    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get("password")
        password_confirm = data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords must match")
        
        return data