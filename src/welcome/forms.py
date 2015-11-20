from django import forms
from .models import User

class UserSignUpForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['address', 'name', 'password', 'email', 'is_staff']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split('@')
		domain, extension = provider.split('.')
		
		return email