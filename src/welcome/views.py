from django.shortcuts import render
from .forms import UserSignUpForm
# Create your views here.
def welcome(request):

	form = UserSignUpForm(request.POST or None)
	print(request)
	print('valid = ' + str(form.is_valid))
	if form.is_valid():
		print('inside valid')
		instance = form.save(commit=False)
		instance.save()
		print(instance)
	context = {
		"form": form,
	}
	return render(request, "welcome.html", context)