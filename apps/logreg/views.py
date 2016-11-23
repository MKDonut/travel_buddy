from django.shortcuts import render, redirect
from .models import User, UserManager
from django.contrib import messages


def index(request):
	
	return render(request, 'logreg/index.html')

def register_user(request):
	res = User.objects.register_user(request.POST)
	if res["added"]:
		request.session['logged_in']=True
		request.session['user_id']=res["new_user"].id
		messages.success(request, "Hello, {}!".format(res["new_user"].first_name))
		return redirect('trip:index')
	else:
		request.session['logged_in']=False
		for error in res["errors"]:
			messages.error(request, error)
		return redirect('trip:index')
def login_user(request):
	print("Something")
	reqs = User.objects.Login_user(request.POST)
	if reqs["checked"]:
		request.session['logged_in']=True
		request.session['user_id']=reqs["logger"].id
		messages.success(request, "Hello, {}!".format(reqs["logger"].first_name))
		return redirect('trip:index')
	else:
		for error in reqs["errors"]:
			request.session['logged_in']=False
			messages.error(request, error)
		return redirect('my_users:index')

def success(request):
	if not request.session['logged_in']:
		return redirect('my_users:index')
	return render(request,'trip/index.html')

def logout(request):
	request.session.clear()
	return redirect('my_users:index')
# Create your views here.
