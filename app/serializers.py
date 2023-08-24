from .models import NameModel
from rest_framework import serializers


class NameSerizlizer (serializers.ModelSerializer):
    class Meta :
        model = NameModel
        fields = '__all__'