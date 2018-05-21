import json

from rest_framework import serializers
from .models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('id', 'ifsc', 'bank_id', 'bank_name', 'branch', "address", "city", "district", "state")
