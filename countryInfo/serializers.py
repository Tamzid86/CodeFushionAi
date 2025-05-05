from rest_framework import serializers
from .models import AllData

class AllDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllData
        fields='__all__'