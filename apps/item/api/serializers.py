from rest_framework import serializers
from apps.item import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ("id", "name", "price", "description")


class ItemsTotalPriceSerializer(serializers.Serializer):
    items = serializers.ListField(child=serializers.IntegerField())

    def validate(self, attrs):
        self.items = models.Item.objects.filter(id__in=attrs["items"])

        if len(self.items) != len(attrs["items"]):
            raise serializers.ValidationError('Invalid Item IDs.')
        return attrs

    def calculate_total(self, **kwargs):
        total_price = sum([item.price for item in self.items])
        return {"total_price": total_price}
