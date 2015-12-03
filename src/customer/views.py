from django.shortcuts import render
from django_tables2   import RequestConfig
from welcome import models
from . import tables
from .forms import EditUserForm
from welcome import forms
import json
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
# Create your views here.
def customer(request):

	#get logged in user
	UserID = request.session.get('UserID')
	if str(UserID) == "guest": #If they're not logged in, redirect to Welcome (guest) page
		return HttpResponseRedirect(reverse('welcome'))
	current_user = models.User.objects.get(id=UserID)

	#set variable for data passed by form
	product_name = request.POST.get('Search_Products')
	selected_products = request.POST.get('selected_products')
	product_updates = request.POST.get('update_info')

	#variables to pass to the DOM
	show_proceed_to_payment_button = False
	tally_products = False

	#set whether or not the "return to staff page" button is displayed
	if current_user.is_staff: 
		staff_display = "display: block"
	else: 
		staff_display = "display: none"
	staff_URL = reverse('admin:app_list', args=("welcome",))


	# change table to show products that match search query, or all if blank
	if product_name:
		table = tables.ProductTable(models.Product.objects.filter(name__contains=product_name, active=True))
	else:
		table = tables.ProductTable(models.Product.objects.filter(active=True))
		show_proceed_to_payment_button = True

	if selected_products:
		show_proceed_to_payment_button = False
		tally_products = True
		p = json.loads(selected_products)
		# create order, add products to order
		new_order = models.customerOrder(user=current_user, paid=False)
		new_order.save()
		for i in p:
			contain = models.Contain(customerOrder=new_order, product=models.Product.objects.get(id=i, active=True), quantity=0)
			contain.save()

		#switch out table to show products in the order.
		#allow quantities of products to be edited.
		table = tables.ContainTable(models.Contain.objects.filter(customerOrder=new_order))


	if product_updates:
		show_proceed_to_payment_button = False
		product_updates = json.loads(product_updates)
		index = 0
		saved = False
		while index < product_updates["length"]:
			ord_id = product_updates[str(index)][0]
			pr_id = product_updates[str(index)][1]
			quant = product_updates[str(index)][2]
			try:
				contain_obj = models.Contain.objects.get(product=models.Product.objects.get(id=int(pr_id), active=True), customerOrder=models.customerOrder.objects.get(pk=int(ord_id)))
			except models.Product.DoesNotExist or models.Contain.DoesNotExist or models.customerOrder.DoesNotExist:
				contain_obj = None
			if contain_obj:
				contain_obj.quantity = int(quant)
				order_obj = models.customerOrder.objects.get(pk=int(ord_id))
				order_obj.paid = True
				prod_obj = models.Product.objects.get(pk=int(pr_id))
				prod_obj.stockQuantity = prod_obj.stockQuantity - int(quant)
				if prod_obj.stockQuantity < 0:
					order_obj.delete()
					messages.add_message(request, messages.INFO, 'You ordered more than the stock quantity. Returning to order page.')
					return HttpResponseRedirect(reverse('customer'))

				if int(quant) == 0:
					order_obj.delete()
					messages.add_message(request, messages.INFO, 'You can\'t order 0 products. Returning to customer page.')
					return HttpResponseRedirect(reverse('customer'))

				order_obj.save()
				contain_obj.save()
				prod_obj.save()
				saved = True

			else:
				print("Product or Contain or CustomerOrder does not exist!")
			index += 1;

		if saved:
			messages.add_message(request, messages.INFO, 'Order Saved.')
		if current_user.is_staff:
			return HttpResponseRedirect(staff_URL)
		else:
			return HttpResponseRedirect(reverse('customer'))
		
	# if update_order_quantity:
	show_search = False
	RequestConfig(request).configure(table)
	context = {
		'table'							: table,
		'product_search_form' 			: forms.ProductSearchForm,
		'select_products_form' 			: forms.ProductSelectForm,
		'user_name'						: current_user.name,
		'show_search'					: show_search,
		'tally_products'				: tally_products,
		'update_order_form'				: forms.UpdateOrderForm,
		'selected_products'				: show_proceed_to_payment_button,
		'staff_display'					: staff_display,
		'staff_URL'						: staff_URL,

	}
	return render(request, "customer.html", context)

def customer_edit_user(request):
	UserID = request.session.get('UserID')
	if str(UserID) == "guest": #If they're not logged in, redirect to Welcome (guest) page
		return HttpResponseRedirect(reverse('welcome'))
	current_user = models.User.objects.get(id=UserID)
	delete_user = request.GET.get("delete_user")

	if current_user.is_staff:
		return_URL = reverse('admin:app_list', args=("welcome",))
	else:
		return_URL = reverse('customer')

	form = EditUserForm(request.POST or None, instance=current_user)
	extra = ""
	if form.is_valid():
		print ("FORM IS VALID")
		#check to see whether that user already exists.
		if models.User.objects.filter(email=form.cleaned_data['email']).exclude(id=UserID): #If this set is not empty, than this user already exists.
			extra ="A user already exists with this email. Changes not saved."
		else:
			print ("IN ELSE")
			form.save()
			if form.cleaned_data['is_staff']:
				return HttpResponseRedirect(reverse('admin:app_list', args=("welcome",)))
			else:
				return HttpResponseRedirect(reverse('customer'))

	if delete_user:
		current_user.delete()
		messages.add_message(request, messages.INFO, 'Account has been deleted.')
		return HttpResponseRedirect(reverse('welcome'))

	context = {
		"form": form,
		"extra": extra,
		"return_URL": return_URL,
		'delete_user_form': forms.DeleteUserForm
	}
	return render(request, "customer_edit_user.html", context)