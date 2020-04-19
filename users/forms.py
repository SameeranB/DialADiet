from allauth.account.forms import SignupForm, LoginForm
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from captcha.fields import ReCaptchaField


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        # self.fields['email'].widget.attrs.update({'class': 'email-input', 'placeholder': 'Email'})
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs.update({'placeholder': "Password", 'class': "input"})
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({'placeholder': "Confirm Password", 'class': "input"})

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Email", 'class': "input"}))
    first_name = forms.CharField(max_length=30, label='',
                                 widget=forms.TextInput(attrs={'placeholder': "First Name", 'class': "input"}))
    last_name = forms.CharField(max_length=30, label='',
                                widget=forms.TextInput(attrs={'placeholder': "Last Name", 'class': "input"}))
    phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'placeholder': "Phone Number", 'class': "input"}),
                             label='',
                             required=True, initial='+91')
    password1 = forms.CharField(max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': "input"}))
    password2 = forms.CharField(max_length=50,
                                widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password", 'class': "input"}))
    captcha = ReCaptchaField(label='', widget=ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'small',
        }
    ))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({'class': 'input', 'placeholder': 'Email'})
        self.fields['login'].label = ''

    password = forms.CharField(max_length=100, label='',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'input', 'placeholder': 'Password'}))
