
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField 
# Create your models here.
from PIL import Image

class etudiant(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    parcours= models.CharField( default ='Math',max_length=70)
    filiere = models.CharField(default ='SRI', max_length=70)
    tel = PhoneNumberField(default ='+242064036047',null =True)
    sexe = models.CharField(default="Masculin",max_length=70)
    image = models.ImageField(upload_to='images',blank=True)
    Actif = models.BooleanField(default = True)
    date = models.DateField(null =True)
    prix = models.DecimalField(max_digits=20000,decimal_places=2,default=19650)



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img= Image.open(self.image.path)

        img.resize((300,100))
        img.save(self.image.path)


    class Meta:
        verbose_name =("etudiant")
        verbose_name_plural =("etudiants")
    
    

     
      
    def __str__(self) :
        return self.nom
    
sex= [
    ('M','Masculin'),
    ('F','Feminin')
]

class client(models.Model):
    nom =models.CharField(max_length =50)
    prenom =models.CharField(max_length =50)
    description =models.CharField(max_length =50)

    class Meta:
        verbose_name=('client')
        verbose_name_plural=('clients')

    def __str__(self) :
        return self.nom    

class commander(models.Model):
    
    agent = models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    email=models.EmailField()
    total = models.CharField(max_length=100)
    tel= PhoneNumberField(default ='+242064036047')
    sexe = models.CharField(max_length=100,choices= sex)
    age = models.CharField(max_length=100)
    adresse= models.CharField(max_length=100)
    quartier= models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    class  Meta:
        ordering =['-date']

