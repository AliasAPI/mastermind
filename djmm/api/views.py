from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BacktestSerializer
from .models import Backtest

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior for our REST API."""
    queryset = Backtest.objects.all()
    serializer_class = BacktestSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Save the post data when creating a new backtest."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the GET, PUT, and DELETE requests."""
    queryset = Backtest.objects.all()
    serializer_class = BacktestSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
