
import django_tables2 as tables
from welcome import models

class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class ProductTable(tables.Table):
	selection = CheckBoxColumnWithName(accessor="pk", attrs = { "td__input": 
                                        {"onclick": "toggle(this)"}},
                                        orderable=False)

	class Meta:
		model = models.Product
		attrs = {"class": "paleblue"}
		fields = ("name", "supplier", "description", "price", "stockQuantity", "selection")
		sequence = ("name", "supplier", "description", "price", "stockQuantity", "selection")


# shows products that are in an order. Allows quantities to be edited.
class ContainTable(tables.Table):
	order_id = tables.Column(accessor="customerOrder.pk")
	product_id = tables.Column(accessor="product.pk")
	product_name = tables.Column(accessor="product.name")
	product_description = tables.Column(accessor="product.description")
	product_price = tables.Column(accessor="product.price")
	product_stockQuantity = tables.Column(accessor="product.stockQuantity")
	order_quantity = tables.TemplateColumn('<input type="number" pattern="[0-9]*" value="0">', verbose_name="Quantity")
	product_supplier = tables.Column(accessor="product.supplier.pk")

	class Meta:
		model = models.Contain
		
		attrs = {"class": "paleblue"}
		fields = ("order_id", "product_id","product_supplier", "product_name", "product_description", "product_stockQuantity")
		sequence = ("order_id", "product_id", "product_supplier", "product_name", "product_description", "product_stockQuantity")