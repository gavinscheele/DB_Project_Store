from django.shortcuts import render
from . import models
from django_tables2   import RequestConfig
from . import tables
from . import forms
# Create your views here.
def welcome(request):
	request.session['UserID'] = "guest" #Initially, ID is guest.
	product_name = request.POST.get('Search_Products')
	if product_name:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=product_name, active=True))
	else:
		table = tables.ProductTable(models.Product.objects.filter(active=True))

	print(request)
	RequestConfig(request).configure(table)
	context = {
		'table'	:	table,
		'product_search_form' : forms.ProductSearchForm,

	}
	return render(request, "welcome.html", context)