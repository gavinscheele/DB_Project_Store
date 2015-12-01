from django import forms


class ProductSearchForm(forms.Form):
	Search_Products = forms.CharField(max_length=50)


	