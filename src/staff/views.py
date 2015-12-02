from django.shortcuts import render
from django_tables2   import RequestConfig
from welcome import models
from . import tables
from welcome import forms
import json
# Create your views here.
def staff(request):
	UserID = request.session.get('UserID')
	product_name = request.POST.get('Search_Products')
	selected_products = request.POST.get('selected_products')
	if product_name:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=product_name))
	else:
		table = tables.ProductTable(models.Product.objects.all())

	if selected_products:
		p = json.loads(selected_products)
		print(p[0])

	print(request)
	RequestConfig(request).configure(table)
	context = {
		'table'	:	table,
		'product_search_form' : forms.ProductSearchForm,
		'select_products_form' : forms.ProductSelectForm

	}
	return render(request, "staff.html", context)