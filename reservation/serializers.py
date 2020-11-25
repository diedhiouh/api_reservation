from django.contrib.auth.models import User 
from rest_framework import serializers

# class UserSerializers(serializers.HyperlinkedModelSerializer):
    
#     class Meta:
#         model = User
#         fields = '__all__'
#         extra_kwargs = {'password' : {'write_only':True, 'required': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

class userSerializers(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields =  '__all__'
        extra_kwargs = {'password' : {'write_only':True, 'required': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



