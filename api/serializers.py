from django.forms import fields
from rest_framework import serializers
from api.models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock',
        )

        def valiadte_price(self, value):
            if value <= 0:
                raise serializers.ValidationError(
                    "Price must be greater than 0")
            return value
