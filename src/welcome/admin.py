from django.contrib import admin

# Register your models here.
from .models import User, Order, Supplier, Product, Contain

class UserAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "address", "name", "password", "email", "is_staff"]

admin.site.register(User, UserAdmin)

class OrderAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "user", "date", "paid"]

admin.site.register(Order, OrderAdmin)

class SupplierAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "name"]

admin.site.register(Supplier, SupplierAdmin)

class ProductAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "supplier", "active", "description", "stockQuantity", "price", "name"]

admin.site.register(Product, ProductAdmin)

class ContainsAdmin(admin.ModelAdmin):	#show multiple fields in the admin
	list_display = ["__str__", "order", "product", "quantity"]

admin.site.register(Contain, ContainsAdmin)