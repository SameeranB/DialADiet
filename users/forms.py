from allauth.account.forms import SignupForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomSignupForm(SignupForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': "Email"}))
    first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': "First Name"}))
    last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': "Last Name"}))
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'placeholder': "Phone Number"}), label='',
                             required=True, initial='+91')
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password"}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        user.save()
        return user
