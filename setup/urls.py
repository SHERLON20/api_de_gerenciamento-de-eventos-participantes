from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from eventin.views import Eventoviewset,Participanteviewset,inscricaoviewset,Listainscricoesparticipanteviewset,Listainscricoeseventoviewset
router = routers.DefaultRouter()
router.register('eventos',Eventoviewset,basename='Eventos')
router.register('participantes',Participanteviewset,basename='Participantes')
router.register('inscricoes',inscricaoviewset,basename='inscrições')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('participantes/<int:pk>/inscricoes',Listainscricoesparticipanteviewset.as_view()),
    path('eventos/<int:pk>/inscricoes',Listainscricoeseventoviewset.as_view())
]
