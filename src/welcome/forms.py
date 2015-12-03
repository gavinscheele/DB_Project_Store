from django import forms
from . import models


class ProductSearchForm(forms.Form):
	Search_Products = forms.CharField(max_length=50)

class ProductSelectForm(forms.Form):
	selected_products = forms.CharField(max_length=50)

class ContainsAdminForm(forms.ModelForm):
	def clean(self):  #Validation to stop staff from ordering more of a product than is available in stock.
		cleaned_data = super(ContainsAdminForm, self).clean()
		formProduct = cleaned_data.get("product")
		formQuantity = cleaned_data.get("quantity")
		if formProduct and formQuantity:
			actualQuantity = models.Product.objects.get(id=formProduct.id).stockQuantity
			if (actualQuantity - formQuantity < 0):
				raise forms.ValidationError("You cannot order this many. There are only " + str(actualQuantity) + " of this item in stock.")

class UserAdminForm(forms.ModelForm):
	def clean(self):  #Validation to stop staff from adding a user with an email that is already in the system.
		cleaned_data = super(UserAdminForm, self).clean()
		formEmail = cleaned_data.get("email")
		if formEmail:
			if models.User.objects.filter(email=formEmail): #If the set is not empty, there is already a user with this email.
				raise forms.ValidationError("There is already a user with this email address.")
