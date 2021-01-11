from rest_framework import serializers, fields
from ..models import Order

"""

Serializers are used for “translating” Django models into other formats like XML, json


"""


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

