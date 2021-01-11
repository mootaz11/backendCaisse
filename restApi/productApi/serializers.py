from rest_framework import serializers,fields
from ..models import Product

"""
Serializers are used for “translating” Django models into other formats like XML, json


"""


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

