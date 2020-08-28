from rest_framework import viewsets, permissions
from app3.models import * 
from app3.api.serializers import * 
from app3.api.permissions import * 

class ClassName_ViewSet(viewsets.ModelViewSet): 
    permission_classes = [ClassName_Permission]
    queryset = ClassName.objects.all()
    serializer_class = ClassName_Serializer

