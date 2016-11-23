from django.shortcuts import render, redirect
from .models import Trip
from ..logreg.models import User
from django.contrib import messages

def index(request):
	if "user_id" not in request.session:
		return redirect("my_users:index")
	context={
		"my_trips":Trip.objects.filter(created_user=request.session["user_id"]) | Trip.objects.filter(all_users=request.session["user_id"]),
		"others_trips":Trip.objects.all().exclude(created_user=request.session["user_id"]).exclude(all_users=request.session["user_id"])
	}
	return render(request, "trip/index.html", context)

def plan(request):
	if "user_id" not in request.session:
		return redirect("my_user:index")
	return render(request, "trip/plan.html")

def add(request):
	user_id=request.session["user_id"]
	response=Trip.objects.trip_validation(request.POST, user_id)
	if response["added"]:
		return redirect("trip:index")
	else:
		for error in response["errors"]:
			messages.error(request, error)
		return redirect("trip:plan")

def join(request,id):
	user=User.objects.get(id=request.session["user_id"])
	trip=Trip.objects.get(id=id)
	trip.all_users.add(user)
	return redirect("trip:index")

def destination(request, id):
	if "user_id" not in request.session:
		return redirect("my_user:index")
	context={
		"trip":Trip.objects.get(id=id),
		"joiners":User.objects.filter(trips=id)	
	}
	return render(request, "trip/destination.html", context)

# Create your views here.
