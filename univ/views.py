from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from univ.models import etudiant,client
from univ.form import etud,create_p,log_u,personne
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from univ.models import commander

# Create your views here.
def requette(request):
    print(request)
    return HttpResponse("cet etudiant n'existe pas !")

@login_required
def test(request):
    #number = request.session.get('visit',0) + 1
    #request.session['visit']=number
    #if number > 4:
        #del(request.session['visit'])
    premier = etudiant.objects.all().order_by('nom')

    #ce script permet de faire une barre de recherche
    if request.method =='GET':
        name = request.GET.get('recherche')

        if name is not None and name != '':
            premier = etudiant.objects.filter(nom__icontains = name)

    # ce script permet d'affichier 4 etudiant par page
    paginator = Paginator(premier , 4)
    page =  request.GET.get('page')

    premier = paginator.get_page(page)

    dico = {
        "etudiant" : premier,
        #"number": number
    }
    return render(request,'univ/source.html',dico)

@login_required
def fr(request):
    p=etud(request.POST or None)
    messages =''
    #if request.method =="POST":
    if p.is_valid():
       p.save()
       p=etud()
    #f= create_p()
       messages ='vos informations on été recu avec succès'
    #if request.method =="POST":
        #f=create_p(request.POST)
        #if f.is_valid():
            #new = etudiant.objects.create(** f.cleaned_data)
            #new.save()
           # messages ="vos informations on été recu avec succès"
            #f= create_p()
      
    return render(request ,'univ/create.html',{'moi':p,'message':messages})

@login_required
def update(request, id):
    try:
       obj = etudiant.objects.get(pk=id)
    except etudiant.DoesNotExist:
        return HttpResponseRedirect(reverse('nouveau'))
    p=etud(request.POST or None, instance=obj)
    messages =''
    if p.is_valid():
       p.save()
       p=etud()
       messages ='vos informations on été modifier avec succès'
    return render(request ,'univ/modifier.html',{'moi':p,'message':messages})

@login_required
def supprimer(request,id):
    if request.method == 'POST':
        obj=etudiant.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect(reverse('tester'))
    

def registrer(request):
    form = log_u()
    if request.method =='POST':
        form = log_u(data=request.POST)
        if form.is_valid():
            form.save()  
            return  redirect('login')

    return render(request,'univ/registre.html',{'form':form})


def connexion(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request," Bienvenue")
            return redirect('tester')
        else:
            messages.error(request," erreur d'authentification")
    return render(request,'univ/login.html')



@login_required
def deconnexion(request):
  logout(request)
  return redirect('login')

def pers(request):
    form = personne()
    if request.method == "POST":
        form = personne(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(request,'univ/test.html',{'form':form})

# la vue vers mes reservations

def reser(request):
    if request.method == "POST":
        element = request.POST.get('element')
        total = request.POST.get('total')
        nom= request.POST.get('nom')
        email= request.POST.get('Email')
        tel = request.POST.get('Phone')
        sexe = request.POST.get('sexe')
        age = request.POST.get('Age')
        adresse = request.POST.get('Adresse')
        quartier = request.POST.get('quartier')

        com = commander(agent=element,nom=nom,email=email,total=total,tel=tel,sexe=sexe,age=age,adresse=adresse,quartier=quartier)
        com.save()
        return redirect('confirmation')



    return render(request,'univ/verifier.html')

def confirmation(request):
    per= commander.objects.all()[:1]
    for item in per:
        nom = item.nom
        
    
    return render(request,'univ/remercier.html',{'nom':nom})
    
