from django.db.models.signals import pre_delete
from django.dispatch import receiver
from welcome.models import Product

#pre_delete.connect(my_callback)

@receiver(pre_delete, sender=Product)
def my_callback(sender, **kwargs):
	print ("something else")
	print (kwargs.signal.description)
	for key, value in kwargs.iteritems():
		print ("%s = %s" % (key,value))

