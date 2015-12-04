
import django_tables2 as tables
from . import models


class ProductTable(tables.Table):
    class Meta:
        model = models.Product
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
        fields = ("name", "description", "price", "stockQuantity")
        sequence = ("name", "description", "price", "stockQuantity")