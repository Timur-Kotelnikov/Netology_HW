from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from .models import Adv
from .permissions import IsOwnerOrStaff
from .serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwnerOrStaff]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

