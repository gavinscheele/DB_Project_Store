from django.db import models

# Create your models here.
class User(models.Model):
	address = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	is_staff = models.BooleanField()
	
	def __str__(self):
		return str(self.id)
    	

class customerOrder(models.Model):
	user = models.ForeignKey(User)
	createDate = models.DateTimeField(auto_now_add=True)
	paid = models.BooleanField()

	def __str__(self):
		return str(self.id)


class Supplier(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.id)


class Product(models.Model):
	customerOrders = models.ManyToManyField(customerOrder, through='Contain')
	active = models.BooleanField()
	description = models.CharField(max_length=100)
	stockQuantity = models.IntegerField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	name = models.CharField(max_length=100)
	supplier = models.ForeignKey(Supplier)

	# @property 
	# def product_id(self):
	# 	return self.id

	def __str__(self):
		#return '%s %s' % (self.id, self.description)
		return str(self.id)


class Contain(models.Model):
	customerOrder = models.ForeignKey(customerOrder, default='1')
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()


	def __str__(self):
		return '%s %s' % (self.id, self.customerOrder)
