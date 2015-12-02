from django.shortcuts import render
from django_tables2   import RequestConfig
from welcome import models
from . import tables
from . import forms
import json

def staff(request):
	UserID = request.session.get('UserID')
	productTable = tables.ProductTable(models.Product.objects.all())
	orderTable = tables.OrderTable(models.customerOrder.objects.all())
	userTable = tables.UserTable(models.User.objects.all())


	context = {
		'userTable'	:	userTable,
		'productTable'	:	productTable,
		'orderTable'	:	orderTable
	}
	return render(request, "staff.html", context)