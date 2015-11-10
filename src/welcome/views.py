from django.shortcuts import render

# Create your views here.
def welcome(request):
	context = {
		
	}
	return render(request, "welcome.html", context)