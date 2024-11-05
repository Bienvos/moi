from django.conf import settings
from django.urls import path
from univ import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.connexion,name='login'),
    #path('news', views.requette,name='nouveau'),
    path('teste', views.test,name='tester'),
    path('ajouter', views.fr,name='formulaire'),
    path('<int:id>/', views.update,name='updata'),
    path('supprimer/<int:id>', views.supprimer,name='supprime'),
    path('registre', views.registrer,name='registre'),
    path('login', views.connexion,name='login'),
    path('securite',views.pers, name='securite'),
    path('logout', views.deconnexion,name='logout'),
    path('reservation', views.reser,name='reservation'),
    path('confirmation',views.confirmation,name='confirmation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)