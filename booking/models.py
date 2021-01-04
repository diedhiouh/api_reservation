# from django.db import models
from djongo import models
from django.utils import timezone
import datetime


# Create your models here.
class Piece(models.Model):
    idpiece =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # id =  models.ObjectIdField()
    matricule = models.CharField(max_length = 100, unique=True)
    etage = models.IntegerField()
    typep = models.CharField(max_length = 100)
    num_tel = models.CharField(max_length = 100)
    nbre_place = models.CharField(max_length = 100)
    equipement = models.CharField(max_length = 100)
    description = models.CharField(max_length = 100)
    nbre_lits = models.CharField(max_length = 100)
    montant = models.IntegerField()
    libre = models.BooleanField(default= True)
    createdAt = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.matricule

class Facture(models.Model):
    id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    titre = models.CharField(max_length = 100)
    libelle = models.CharField(max_length = 100)
    montant = models.IntegerField()
    description = models.CharField(max_length = 100)
    actif = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.titre

class Client(models.Model):
    id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # id =  models.ObjectIdField()
    prenom = models.CharField(max_length = 100)
    nom = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    cni = models.CharField(max_length = 100)
    sexe = models.CharField(max_length = 100)
    actif = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default = timezone.now)


    def __str__(self):
        return self.prenom + ' ' + self.nom


class Reserve(models.Model):
    # id =  models.ObjectIdField()
    id =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    piece = models.ForeignKey(Piece , on_delete=models.PROTECT)
    facture = models.ForeignKey(Facture , on_delete=models.PROTECT)
    client = models.ForeignKey(Client,  on_delete=models.PROTECT)
    nbre_personne = models.CharField(max_length=100)
    debut_sejour = models.CharField(max_length=100)
    fin_sejour = models.CharField(max_length=100)
    date_reserve = models.DateField(auto_now_add = True)
    description = models.CharField(max_length=100)
    actif = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.id