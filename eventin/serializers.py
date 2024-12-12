from rest_framework import serializers
from .models import Evento,Participante,Inscricao

class Eventoserializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id','titulo','descricao','local','data_evento','capacidade']
class Participanteserializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['id','nome','cpf','email','telefone']

    def validate_nome(self,nome):
        if not nome.replace(' ','').isalpha():
            raise serializers.ValidationError('o nome só pode conter letras e espaço')
        if len(nome)<3:
            raise serializers.ValidationError('o nome deve conter 3 caracters ou mais')
        return nome
    def validate_email(self,email):
        if '@'not in email or '.' not in email.split('@')[-1]:
            raise serializers.ValidationError('o email deve ser válido')
        return email
    def validate_telefone(self,telefone):
        if len(telefone)<10 or not telefone.isdigit():
            raise serializers.ValidationError(f'o telefone:{telefone} deve ter pelo menos 10 digitos e so pode ser numero')
        return telefone

class Isncricaoserializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['id','evento','participante','data_inscricao']
        
class Listainscricoesparticipantesserializer(serializers.ModelSerializer):
    evento= serializers.ReadOnlyField(source='evento.titulo')
    class Meta:
        model = Inscricao
        fields = ['evento','data_inscricao']

class Listainscricoeseventoserializer(serializers.ModelSerializer):
    participante= serializers.ReadOnlyField(source='participante.nome')
    class Meta:
        model = Inscricao
        fields = ['participante','data_inscricao',]

class participanteserializersv2(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = ['id','nome','email','telefone']
        