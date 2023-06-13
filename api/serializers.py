from rest_framework import serializers
from vishome.models import item
from vishome.models import contactdet

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=item
        fields='__all__'

class ContactdetSerializer(serializers.ModelSerializer):
    class Meta:
        model=contactdet
        fields='__all__'