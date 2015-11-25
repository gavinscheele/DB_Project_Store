from django.shortcuts import render
from .forms import UserSignUpForm
# Create your views here.
def welcome(request):

	form = UserSignUpForm(request.POST or None)
	print(request)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		"form": form,
	}
	return render(request, "welcome.html", context)