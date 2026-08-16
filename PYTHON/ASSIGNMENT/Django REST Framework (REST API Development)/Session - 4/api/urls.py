from django.urls import path

from .views import (
    PlaylistView,
    OrderView,
    CartView,
    TicketView
)

urlpatterns = [
    path('playlists/', PlaylistView.as_view()),
    path('orders/', OrderView.as_view()),
    path('cart/', CartView.as_view()),
    path('tickets/', TicketView.as_view()),
]