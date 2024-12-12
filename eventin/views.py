from rest_framework import viewsets,generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Evento,Participante,Inscricao
from .serializers import Eventoserializer,Participanteserializer,Isncricaoserializer,Listainscricoeseventoserializer,Listainscricoesparticipantesserializer,participanteserializersv2

class Eventoviewset(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = Eventoserializer
    
class Participanteviewset(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Participante.objects.all()
    #serializer_class = Participanteserializer
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return participanteserializersv2
        else:
            return Participanteserializer
class inscricaoviewset(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Inscricao.objects.all()
    serializer_class = Isncricaoserializer
    
class Listainscricoesparticipanteviewset(generics.ListAPIView):
    serializer_class = Listainscricoesparticipantesserializer
    
    def get_queryset(self):
        participante_id =self.kwargs['pk']
        return Inscricao.objects.filter(participante_id=participante_id)

class Listainscricoeseventoviewset(generics.ListAPIView):
    serializer_class = Listainscricoeseventoserializer
    
    def get_queryset(self):
        evento_id =self.kwargs['pk']
        return Inscricao.objects.filter(evento_id=evento_id)




# from django.http import JsonResponse
# def participantes(request):
#     if request.method == 'GET':
#         participante = {
#             'id':1,
#             'nome':'fulano'
#         }
#         return JsonResponse(participante)