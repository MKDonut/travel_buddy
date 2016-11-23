from __future__ import unicode_literals
from ..logreg.models import User, UserManager
import datetime
from django.db import models

class TripManger(models.Manager):
	def trip_validation(self, data, user_id):
		errors=[]
		if not data["destination"]or not data["description"] or not data ["date_from"] or not data["date_to"]:
			errors.append("Please fill out all entry fields!")
		if data["date_from"] > data["date_to"]:
			errors.append("Ooops! You can't comeback before you go")
		elif data["date_from"] < str(datetime.date.today()):
			errors.append("Ooops, are you trying to time travel?")

		response={}
		if not errors:
			self.create(destination=data["destination"], description=data["description"], date_from=data["date_from"], date_to=data["date_to"], created_user=User.objects.get(id=user_id))
			response["added"]=True
		else:
			response["added"]=False
			response["errors"]=errors
		return response

class Trip(models.Model):
	destination= models.CharField(max_length=255)
	description= models.CharField(max_length=500)
	date_from= models.DateField()
	date_to= models.DateField()
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)
	created_user= models.ForeignKey(User, related_name="users")
	all_users=models.ManyToManyField(User, related_name="trips")
	objects=TripManger()
# Create your models here.
