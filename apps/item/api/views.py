from rest_framework import status, viewsets
from apps.item.api.serializers import ItemSerializer, ItemsTotalPriceSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.item.models import Item


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()


class ItemPriceSumViewSet(CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ItemsTotalPriceSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.calculate_total()
        return Response(data=data, status=status.HTTP_200_OK)
