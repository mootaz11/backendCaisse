from rest_framework import serializers, fields
from ..models import Ticket
"""
Serializers are used for “translating” Django models into other formats like XML, json


"""
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields='__all__'

