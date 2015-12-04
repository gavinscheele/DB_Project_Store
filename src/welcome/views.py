from django.shortcuts import render
from . import models
from django_tables2   import RequestConfig
from . import tables
from . import forms
# Create your views here.
def welcome(request):
	request.session['UserID'] = "guest" #Initially, ID is guest.
	product_name = request.POST.get('Search_Products')
	show_all = request.POST.get('show_all')

	if product_name:
		request.session['product_search_name'] = product_name

	sorting = request.GET.get('sort')
	print(sorting)

	if (product_name or sorting) and not show_all:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=request.session.get('product_search_name'), active=True))
	else:
		table = tables.ProductTable(models.Product.objects.filter(active=True))


	print(request)
	RequestConfig(request).configure(table)
	context = {
		'table'	:	table,
		'product_search_form' : forms.ProductSearchForm,

	}
	return render(request, "welcome.html", context)