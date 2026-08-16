from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Restaurant
from api.serializers import RestaurantSerializer


class RestaurantPagination(LimitOffsetPagination):
    default_limit = 3


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    # Pagination
    pagination_class = RestaurantPagination

    # Ordering and Filtering
    filter_backends = [OrderingFilter, DjangoFilterBackend]

    ordering_fields = ['name', 'cuisine']

    filterset_fields = ['cuisine']