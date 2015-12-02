from django import forms
from welcome.models import User  #instead of segmenting models based on app, all exist in welcome.models and other apps pull from there.


class UserSignInForm(forms.Form):
		email = forms.EmailField(label='email address')
		password = forms.CharField(label='password', widget=forms.PasswordInput())

class UserSignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['address', 'name', 'password', 'email', 'is_staff']

	# def clean_email(self):
		# email = self.cleaned_data.get('email')
		# email_base, provider = email.split('@')
		# domain, extension = provider.split('.')
		
		# return email

