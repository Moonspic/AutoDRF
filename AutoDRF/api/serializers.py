from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from app3.models import *

class ClassName_Serializer(serializers.ModelSerializer): 
    class Meta: 
        model = ClassName
        fields = '__all__' 

