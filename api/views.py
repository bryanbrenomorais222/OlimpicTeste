from rest_framework.viewsets import ModelViewSet
from .models import (Atleta, NOC, Esporte, Competicao, OliGame, Medalha, Evento)

from .serializers import(AtletaSerializer, NOCSerializer, EsporteSerializer, CompeticaoSerializer, OliGameSerializer, MedalhaSerializer,EventoSerializer)





class NOCViewSet(ModelViewSet):
    queryset = NOC.objects.all()
    serializer_class = NOCSerializer
    filterset_fields = ('id', 'noc', 'regiao','notas')

class EsporteViewSet(ModelViewSet):
    queryset = Esporte.objects.all()
    serializer_class = EsporteSerializer
    filterset_fields = ('id','nome_esporte')

class AtletaViewSet(ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    filterset_fields = ('id','nome', 'altura', 'peso')

class CompeticaoViewSet(ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer
    filterset_fields = ('id','nome_competicao', 'esporte')

class OliGameViewSet(ModelViewSet):
    queryset = OliGame.objects.all()
    serializer_class = OliGameSerializer
    filterset_fields = ('id','ano', 'sede', 'temp')

class MedalhaViewSet(ModelViewSet):
    queryset = Medalha.objects.all()
    serializer_class = MedalhaSerializer
    filterset_fields = ('id','medal')

class EventViewSet(ModelViewSet):
    queryset = Evento.objects.select_related(
            'nome_atleta',
            'atleta_noc',
            'atleta_idade',
            'atleta_time',
            'competicao_nome',
            'tipo_medalha',
    )
    serializer_class = EventoSerializer
