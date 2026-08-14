from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def hello_spotify(request):
    return Response({
        "message": "Hello, Spotify Fans!"
    })





# JSON example:
# {
#     "name": "iPhone 15",
#     "price": 69999
# }

# XML example:
# <product>
#     <name>iPhone 15</name>
#     <price>69999</price>
# </product>
