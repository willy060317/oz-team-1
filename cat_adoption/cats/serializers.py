from rest_framework import serializers
from .models import Cat, HealthRecord

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class CatSerializer(serializers.ModelSerializer):
    health_records = HealthRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Cat
        fields = '__all__'