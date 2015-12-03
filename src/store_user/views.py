from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import UserSignUpForm
from .forms import UserSignInForm
from welcome.models import User

# Create your views here.
def store_user(request):
	request.session['UserID'] = "guest" #Initially, ID is guest. reset this every time they arrive to this page.
	form = UserSignInForm(request.POST or None)
	extra = ""
	print(request)
	if form.is_valid():
		inEmail = form.cleaned_data['email']
		inPassword = form.cleaned_data['password']
		
		if User.objects.filter(email=inEmail, password=inPassword): #If this set is not empty, then this user exists.
			thisUser = User.objects.get(email=inEmail, password=inPassword)
			request.session['UserID'] = thisUser.id
			if thisUser.is_staff: #If the user is staff, take them to the staff page.
				return HttpResponseRedirect(reverse('admin:app_list', args=("welcome",))) #Redirect to "welcome" app in admin page.
			else: #Otherwise, the user is just a customer and is directed to the regular customer view.
				return HttpResponseRedirect(reverse('customer'))
		else: #user does not exist.
			extra = "No user found with these credentials."
	context = {
		"form": form,
		"extra": extra
	}
	return render(request, "store_user.html", context)

def store_user_signup(request):
	#TO RECEIVE: request.session.get('cat')
	#TO GENERATE: request.session['cat'] = True;
	form = UserSignUpForm(request.POST or None)
	extra = ""
	if form.is_valid():
		#check to see whether that user already exists.
		if User.objects.filter(email=form.cleaned_data['email']): #If this set is not empty, than this user already exists.
			extra ="A user already exists with this email. New account not created."
		else:
			instance = form.save(commit=False)
			instance.save()
			return HttpResponseRedirect(reverse('store_user'))
	context = {
		"form": form,
		"extra": extra
	}
	return render(request, "store_user_signup.html", context)