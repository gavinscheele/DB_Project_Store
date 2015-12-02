
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
		fields = ("name", "description", "price", "stockQuantity", "discount", "selection")
		sequence = ("name", "description", "price", "stockQuantity", "discount", "selection")