from rest_framework import serializers
from .models import  Piece,Client,Reserve,Facture
from django.contrib.auth.models import User,Permission,Group



class FactureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Facture
        fields = ('id', 'titre', 'libelle', 'montant' ,'actif','description')

class PieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piece
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Reserve
        fields = '__all__'

class UserSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password' : {'write_only':True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    

class GroupSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields  = '__all__'