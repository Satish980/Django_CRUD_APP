
from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.index, name="index"),
	path("signup/",views.signup, name="signup"),
	path("data/",views.data, name = "data"),
	path("update/<int:id>/",views.update, name = "update"),
	path("deletedata/<int:id>/",views.delete, name = "deletedata"),
	path("logout",views.logout, name="logout"),
]