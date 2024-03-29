from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Adv
from .permissions import IsOwnerOrStaff
from .serializers import AdvSerializer
from .filters import AdvFilter


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwnerOrStaff, IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = AdvFilter
    search_fields = ['title', 'description']
    ordering_fields = ['posted_at', 'status']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

