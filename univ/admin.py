from django.contrib import admin
from .models import etudiant,commander
# Register your models here.
class Adminetud(admin.ModelAdmin):
    list_display =('nom','prenom','parcours','filiere','tel','sexe','image','Actif','date')
    list_editable =('tel',)

class com(admin.ModelAdmin):
    list_display =('agent','nom','email','tel','sexe','age','adresse','total','quartier','date')
    


admin.site.site_header=("UDSN-SRI")
admin.site.site_title =("Sri-Dev")
admin.site.register(etudiant,Adminetud)
admin.site.register(commander,com)


