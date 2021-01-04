from rest_framework import viewsets, generics
from django.contrib.auth.models import Permission, User
from .serializers import userSerializers, RegisterSerializer
from rest_framework.permissions import AllowAny

class userviewsets(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = userSerializers 

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer