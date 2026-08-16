from django.urls import path
from api.views import *


urlpatterns = [
    path("list_restaurant",list_restaurant,name="list_restaurant"),
    path("create_restaurant",create_restaurant,name="create_restaurant"),
    path("delete_restaurant/<id>",delete_restaurant,name="delete_restaurant"),
    path("update_restaurant/<id>",update_restaurant,name="update_restaurant")
]