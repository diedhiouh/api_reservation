from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Reserve)
admin.site.register(Facture)
admin.site.register(Piece)