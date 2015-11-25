# from django.db.models.signals import pre_delete, post_delete
# from django.dispatch import receiver
# from welcome.models import Product, Contain, Order
# import datetime

# #pre_delete.connect(my_callback)
# savedProduct = ""
# savedContain = ""


# @receiver(pre_delete, sender=Product)
# def my_callback1(sender, **kwargs):
# 	print ("something else")
# 	for key, value in kwargs.iteritems():
# 		if key == 'signal':
# 			print(value)

# 		print ("%s = %s" % (key,value))
# 	print("---")
# 	inContains = Contain.objects.filter(product=kwargs.get('instance')) #inContains is all the contain instances with product that was deleted
# 	global savedContain
# 	savedContain = inContains
# 	(inContains)

# 	for o in inContains:
# 		match = Order.objects.get(id = str(o.order)) #match = for each contain doc that was deleted, match is that corresponding doc in order
# 		print(match) #match

# 		print(match.date)

# 		now = datetime.datetime.now()
# 		create_date = match.date.replace(tzinfo=None)
# 		diffInDays = (now - create_date).days
# 		print(diffInDays)
# 		# if some one has ordered the product in the last 31 days, 
# 		# don't delete it. (save and re-add it)
# 		if(diffInDays < 31):
# 			print(kwargs.get('instance'))
# 			global savedProduct
# 			#there is at least one order for the product in the last month.
# 			#don't delete it
# 			savedProduct = Product.objects.get(id=str(kwargs.get('instance')))
# 			print(savedProduct)
# 			break


# @receiver(post_delete, sender=Product)
# def my_callback2(sender, **kwargs):
	
# 	print('post delete')
# 	print(savedProduct)
# 	if savedProduct != "":
# 		print('we in der')
# 		print(savedProduct.description)
# 		p = Product(id = None, active = savedProduct.active, description = savedProduct.description, stockQuantity = savedProduct.stockQuantity,
# 			price = savedProduct.price, name = savedProduct.name, supplier = savedProduct.supplier, discount = savedProduct.discount)
# 		print(p)
# 		p.save()

# 		c = Contain(id = None, Order = , Product = savedProduct.id, Quantity = )
# from django.db.models.signals import pre_delete
# from django.dispatch import receiver
# from welcome.models import Product, Contain, Order
# #pre_delete.connect(my_callback)

# @receiver(pre_delete, sender=Product)
# def my_callback(sender, **kwargs):
# 	#debug
# 	print ("something else")  
# 	for key, value in kwargs.iteritems():
# 		if key == 'signal':
# 			print(value)

# 		print ("%s = %s" % (key,value))

# 	print(kwargs.get('instance'))
# 	print("---")
# 	print(Contain.objects.filter(product=kwargs.get('instance')))
# 	print("---")
# 	ordersInContains = Contain.objects.filter(product=kwargs.get('instance')) #c object Contains with that product ID
# 	print(ordersInContains)

# 	#c.order for c in ordersInContains
# 	for o in ordersInContains:
# 		matches = Order.objects.filter(id = o)
# 		print(matches)

