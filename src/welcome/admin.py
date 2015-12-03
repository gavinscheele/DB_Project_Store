from django.contrib import admin
from .forms import ContainsAdminForm, UserAdminForm

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

admin.site.register(Product, ProductAdmin)

class ContainsAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	form = ContainsAdminForm
	list_display = ["__str__", "customerOrder", "product", "quantity"]

admin.site.register(Contain, ContainsAdmin)