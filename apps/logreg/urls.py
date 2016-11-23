from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register_user$', views.register_user, name="register_user"),
    url(r'^success$', views.success, name="success"),
    url(r'^login_user$', views.login_user, name="login_user"),
    url(r'^logout$',views.logout, name="logout")
]