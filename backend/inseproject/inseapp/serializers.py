from rest_framework import serializers
from .models.inse_model import *

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
        extra_kwargs = {'id_escola': {'read_only': True}}
