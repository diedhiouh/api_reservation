from rest_framework import viewsets
from django.contrib.auth.models import Permission, User
from .serializers import userSerializers

class userviewsets(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = userSerializers 
