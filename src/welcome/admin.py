from django.contrib import admin
from .forms import ContainsAdminForm, UserAdminForm
from datetime import date, timedelta

# Register your models here.
from .models import User, customerOrder, Supplier, Product, Contain

class UserAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	form = UserAdminForm
	list_display = ["__str__", "address", "name", "password", "email", "is_staff"]

admin.site.register(User, UserAdmin)

class customerOrderAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "user", "createDate", "paid"]

admin.site.register(customerOrder, customerOrderAdmin)

class SupplierAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "name"]

admin.site.register(Supplier, SupplierAdmin)

class ProductAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "supplier", "active", "description", "stockQuantity", "price", "name"]
	def has_delete_permission(self, request, obj=None):
		# for key in request.POST:
		# 		value = request.POST[key]
		# for key, value in request.POST.iteritems():
		# 	print (key, value)
		deleteID = request.POST.get("_selected_action");

		today_minus_month = date.today() - timedelta(days=30)

		this_months_orders = customerOrder.objects.filter(createDate__gte=today_minus_month)
		contain = Contain.objects.filter(customerOrder_id__in=this_months_orders, product_id=deleteID) #If something's in this set, it's been ordered recently.
		if contain:
			return False
		else:
		 	return True


admin.site.register(Product, ProductAdmin)

class ContainsAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	form = ContainsAdminForm
	list_display = ["__str__", "customerOrder", "product", "quantity"]

admin.site.register(Contain, ContainsAdmin)