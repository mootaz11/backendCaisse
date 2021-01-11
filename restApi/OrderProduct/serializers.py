from rest_framework import serializers, fields
from ..models import OrderProduct

"""

Serializers are used for “translating” Django models into other formats like XML, json


"""

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderProduct
        fields=['product','quantity','order']

