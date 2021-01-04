"""schoolmanger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import response, request
from .router import router
from .viewset import userSerializers
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework_simplejwt import views as jwt_views
from booking.views import UserAdd
from .viewset import RegisterView

def home(request):
    UserAdd.addUser()
    teste = User.objects.all()
    print('NOMBRE',teste.count())
    if teste.count()==0 :
        print('Aucun utilisateur en cours ')
        superuser = User.objects.create_superuser(
            username='diedhiou',
            email='habibodh@gmail.com',
            password='diedhiou123')
        superuser.save()
    
    return response.HttpResponse('hello')

def sample_view(request):
    
    # current_user = request.user
    # print("COURANT=> "+current_user.id)
    return response.HttpResponse("current_user")


urlpatterns = [
    path('', home),
    path('courant/', sample_view),
    path('admin/', admin.site.urls),
    path('booking/', include(router.urls)),

    path('booking/', include('booking.urls')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'), 
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'), 
    path('booking/register/', RegisterView.as_view(), name='auth_register'),

    
]
