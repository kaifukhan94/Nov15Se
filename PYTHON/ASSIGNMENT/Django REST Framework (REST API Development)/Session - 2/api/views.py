from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import *
from api.serializer import *
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def list_restaurant(request):
    restaurants = Restaurant.objects.all()
    ser = RestaurantSerializer(restaurants,many=True)
    return Response({"data":ser.data},status=status.HTTP_200_OK)


@api_view(['POST'])
def create_restaurant(request):
    ser = RestaurantSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"errors" : ser.errors,"messages":"somethimg went wrong"},status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data":ser.data},status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_restaurant(request, id):

    try:
        restaurant = Restaurant.objects.get(id=id)
    except Restaurant.DoesNotExist:
        return Response(
            {"error": "Restaurant not found"},status=status.HTTP_404_NOT_FOUND)

    restaurant.delete()
    return Response({"message": "Restaurant deleted successfully"},status=status.HTTP_200_OK)



@api_view(['PUT'])
def update_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)
    ser = RestaurantSerializer(restaurant, data=request.data)
    if not ser.is_valid():
        return Response({"errors": ser.errors, "messages": "something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    else:
        ser.save()
        return Response({"data": ser.data},status=status.HTTP_200_OK)

