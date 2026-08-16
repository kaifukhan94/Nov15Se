from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Playlist
from .serializers import PlaylistSerializer


class PlaylistView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        playlists = Playlist.objects.all()

        serializer = PlaylistSerializer(
            playlists,
            many=True
        )

        return Response(serializer.data)



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer


class OrderView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = Order.objects.filter(user=request.user)

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)



from rest_framework.authentication import SessionAuthentication

from .models import CartItem
from .serializers import CartItemSerializer


class CartView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CartItemSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data)

        return Response(serializer.errors, status=400)



from rest_framework.authentication import TokenAuthentication
from .permissions import IsPremiumUser

from .models import Ticket
from .serializers import TicketSerializer


class TicketView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPremiumUser]

    def get(self, request):

        tickets = Ticket.objects.filter(
            user=request.user
        )

        serializer = TicketSerializer(
            tickets,
            many=True
        )

        return Response(serializer.data)