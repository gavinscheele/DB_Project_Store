from django.shortcuts import render

# Create your views here.
def store_user(request):
	#request.session.get('cat')
	context = {

	}
	return render(request, "store_user.html", context)