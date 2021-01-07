from django.contrib import admin
from django.urls import path, include
from .views import *
from django.http import HttpResponse,response
from rest_framework_simplejwt import views as jwt_views 

def booking(request):
    return response.HttpResponse('Booking')

urlpatterns = [
    # path('', 'booking'),
    path('piece/', PieceViewList.as_view()),
    path('piece/<int:pk>', PieceViewEdit.as_view()),
    path('facture/', FactureViewList.as_view()),
    path('facture/<int:pk>', FactureViewEdit.as_view()),
    path('client/', ClientViewList.as_view()),
    path('client/<int:pk>', ClientViewEdit.as_view()),
    path('reserve/', ReserveViewList.as_view()),
    path('reserve/<int:pk>', ReserveViewEdit.as_view()),
    path('utilisateur/', UserViewList.as_view()),
    path('utilisateur/<int:pk>', UserViewEdit.as_view()),
    path('group/' , GroupViewList.as_view()),
    path('group/<int:pk>' , GroupViewSet.as_view()),
]

