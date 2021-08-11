from django.urls import path
from . import views

app_name = "request"

urlpatterns = [
    path("",views.index,name="index"),
    path("popup/",views.p2,name="p2")

]