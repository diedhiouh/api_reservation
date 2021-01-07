from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Permission
from rest_framework.permissions import IsAuthenticated
# from .permissions import *
from django.contrib.auth.models import User, Group, UserManager
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.hashers import make_password


# Create your views here.
class ReserveViewList(generics.ListCreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]

class ReserveViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]

class ClientViewList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class ClientViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

class FactureViewList(generics.ListCreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_classes = [IsAuthenticated]

class FactureViewEdit(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_classes = [IsAuthenticated]

class PieceViewList(generics.ListCreateAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    permission_classes = [IsAuthenticated]

class PieceViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer
    permission_classes = [IsAuthenticated]

class UserViewList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

class UserViewEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

class GroupViewList(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializers
    permission_classes = [permissions.IsAuthenticated]

class UserAdd():
    
    def addUser():
        # create = 0
        # if create == 0:
        #     User.objects.get_or_create(username='diedhiou',email='habibodh@gmail.com',password=make_password(password="diedhiou123"),first_name='Habibou',last_name='DIEDHIOU',is_superuser=True,is_active=True)
        #     create = 1
        pass
    addUser()