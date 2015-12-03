from django import forms


class ProductSelectForm(forms.Form):
	fselected_products = forms.CharField(max_length=50)

class TableTypeForm(forms.Form):
	table_type = forms.CharField(max_length=50)

class UserForm(forms.Form):
	inputt = forms.CharField(max_length=50)