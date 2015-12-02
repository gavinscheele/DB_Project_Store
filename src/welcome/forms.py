from django import forms


class ProductSearchForm(forms.Form):
	Search_Products = forms.CharField(max_length=50)

class ProductSelectForm(forms.Form):
	selected_products = forms.CharField(max_length=50)

	