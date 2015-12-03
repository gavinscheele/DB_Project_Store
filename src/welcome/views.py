from django.shortcuts import render
from . import models
from django_tables2   import RequestConfig
from . import tables
from . import forms
# Create your views here.
def welcome(request):
	#request.session['cat'] = True;
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

#TRYING THIS CODE OUT WITH THIS PLACEMENT. MIGHT NOT BE RIGHT.
# def app_index(request):
# 	messages.add_message(request, messages.INFO, lowStr)
# 	lowProducts = Product.objects.filter(stockQuantity=0);
# 	if lowProducts: #If this set is not empty, then we are low on that product and they need to get an alert.
# 		lowStr = 'You are low on the following products!\n'
# 		for product in lowProducts:
# 			lowStr = lowStr + str(product.name) + "\n"
# 		messages.add_message(request, messages.WARNING, lowStr)