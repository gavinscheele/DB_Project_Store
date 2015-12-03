
import django_tables2 as tables
from welcome import models

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class ProductTable(tables.Table):

	class Meta:
		model = models.Product
		attrs = {"class": "paleblue"}
		fields = ("name", "description", "price", "stockQuantity", "discount", "selection")
		sequence = ("name", "description", "price", "stockQuantity", "discount", "selection")

class UserTable(tables.Table):

	class Meta:
		model = models.User
		attrs = {"class": "paleblue"}
		fields = ("address", "name", "password", "email", "is_staff")
		sequence = ("name", "email", "password", "address", "is_staff")

class OrderTable(tables.Table):
	product = tables.Column(accessor='models.contain.product')
	quantity = tables.Column(accessor='modelscontain.quantity')
	class Meta:
		model = models.customerOrder
		attrs = {"class": "paleblue"}
		fields = ("user", "createDate", "paid")
		sequence = ("user", "createDate", "paid")