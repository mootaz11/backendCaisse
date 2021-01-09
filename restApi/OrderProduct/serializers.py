from rest_framework import serializers, fields
from ..models import OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderProduct
        fields=['product','quantity','order']

