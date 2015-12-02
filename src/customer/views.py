from django.shortcuts import render
from django_tables2   import RequestConfig
from welcome import models
from . import tables
from welcome import forms
# Create your views here.
def customer(request):
	#request.session.get('cat')
	product_name = request.POST.get('Search_Products')
	if product_name:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=product_name))
	else:
		table = tables.ProductTable(models.Product.objects.all())

	print(request)
	RequestConfig(request).configure(table)
	context = {
		'table'	:	table,
		'product_search_form' : forms.ProductSearchForm,

	}
	return render(request, "customer.html", context)