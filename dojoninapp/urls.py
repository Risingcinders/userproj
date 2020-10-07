from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addninja', views.ninjaadd),
    path('adddojo', views.dojoadd),
    path('deletedojo/<int:deleteid>', views.deletedojo)
]
