from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^plan/$', views.plan, name="plan"), 
    url(r'^add/$', views.add, name="add"), 
   	url(r'^destination/(?P<id>\d+)$', views.destination, name="destination"),
   	url(r'^join/(?P<id>\d+)$',views.join, name="join"),
]