from django.shortcuts import render
from django_tables2   import RequestConfig
from welcome import models
from . import tables
from welcome import forms
import json
# Create your views here.
def customer(request):
	#get logged in user
	UserID = request.session.get('UserID')
	current_user = models.User.objects.get(id=UserID)

	#set variable for data passed by form
	product_name = request.POST.get('Search_Products')
	selected_products = request.POST.get('selected_products')

	# change table to show products that match search query, or all if blank
	if product_name:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=product_name))
	else:
		table = tables.ProductTable(models.Product.objects.all())

	if selected_products:
		p = json.loads(selected_products)
		# create order, add products to order
		new_order = models.customerOrder(user=current_user, paid=False)
		new_order.save()
		for i in p:
			contain = models.Contain(customerOrder=new_order, product=models.Product.objects.get(id=i), quantity=0)
			contain.save()

		#switch out table to show products in the order.
		#allow quantities of products to be edited.
		table = tables.ContainTable(models.Contain.objects.all())

	#FOR TESTING ONLY ######################################
	print(models.Contain.objects.all())
	table = tables.ContainTable(models.Contain.objects.all())
	########################################################

	show_search = False
	tally_products = True
	RequestConfig(request).configure(table)
	context = {
		'table'							: table,
		'product_search_form' 			: forms.ProductSearchForm,
		'select_products_form' 			: forms.ProductSelectForm,
		'user_name'						: current_user.name,
		'show_search'					: show_search,
		'tally_products'				: tally_products

	}
	return render(request, "customer.html", context)