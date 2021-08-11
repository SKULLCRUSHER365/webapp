from django.db.models import fields
from rest_framework import serializers
from .models import selection,compounds,currency

class selectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = selection
        fields='__all__'

class compoundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = compounds
        fields='__all__'

class currencySerializer(serializers.ModelSerializer):
    class Meta:
        model = currency
        fields='__all__'