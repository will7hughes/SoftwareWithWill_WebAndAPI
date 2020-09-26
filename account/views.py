from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import UserAuthenticationForm

from dal import autocomplete
from account.models import User

def logout_view(request):
	logout(request)
	return redirect('login')

def login_view(request):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("project/report/list")

	 if request.POST:
	 	form = UserAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		username = request.POST['username']
	 		password = request.POST['password']
	 		user = authenticate(username=username, password=password)

	 		if user:
	 			login(request, user)
	 	return redirect("project/report/list")

	 else:
	 	form = UserAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'account/login.html', context)


class UserAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = User.objects.all()

		if self.q:
			qs = qs.filter(name__icontains=self.q)

		return qs
