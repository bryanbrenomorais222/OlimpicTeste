from rest_framework.serializers import ValidationError, ModelSerializer
from api import models

class AtletaSerializer(ModelSerializer):
    class Meta:
        model = models.Atleta
        fields = ['id','nome', 'altura', 'peso']

class NOCSerializer(ModelSerializer):
    class Meta:
        model = models.NOC
        fields = ['id','noc', 'regiao', 'notas']

class EsporteSerializer(ModelSerializer):
    class Meta:
        model = models.Esporte
        fields = ['id','nome_esporte']

class CompeticaoSerializer(ModelSerializer):
    class Meta:
        model = models.Competicao
        fields = ['id','nome_competicao', 'esporte']
    
        def create(self, validated_data):
            sport_data = validated_data.pop('esporte')

            sport = models.Esporte.objects.get_or_create(**sport_data)

            competition = models.Competicao.objects.create(
                sport=sport,
                **validated_data
                )
            return competition

    def update(self, competition, validated_data):
        sport_data = validated_data.pop('esporte')

        sport_serializer = EsporteSerializer(
            competition.sport,
            sport_data
        )
        if sport_serializer.is_valid(): 
            sport_serializer.save()
        else:
            ValidationError(sport_serializer.errors)
        
        competition.nome = validated_data.get('nome', competition.nome)
        competition.save()

        return competition


class OliGameSerializer(ModelSerializer):
    class Meta:
        model = models.OliGame
        fields = ['id','ano', 'sede', 'temp']
        
class MedalhaSerializer(ModelSerializer):
    class Meta:
        model = models.Medalha
        fields = ['id','medal']

class EventoSerializer(ModelSerializer):

    atl = AtletaSerializer(many=False)
    ath_NOC = NOCSerializer(many=False)
    olgame = OliGameSerializer(many=False)
    comp = CompeticaoSerializer(many=False)
    medalha = MedalhaSerializer(many=False)
    
    class Meta:
        model = models.Evento
        fields = [
            'id',
            'nome_atleta',
            'atleta_noc',
            'competicao_nome',
            'tipo_medalha',
            ]
    
    def create(self, validated_data):
        atleta_data = validated_data.pop('atleta')
        noc_data = validated_data.pop('atleta_noc')
        competition_data = validated_data.pop('competicao_nome')
        medal_data = validated_data.pop('tipo_medalha')


        athlete = models.Atleta.objects.get_or_create(**atleta_data)
        noc = models.NOC.objects.get_or_create(**noc_data)
        medal = models.Medalha.objects.get_or_create(**medal_data)

        event = models.Evento.objects.create(
            athlete=athlete,
            athlete_NOC=noc,
            medal=medal,
            **validated_data
            )

        return event
    
    def update(self, event, validated_data):

        atleta_data = validated_data.pop('athlete')
        noc_data = validated_data.pop('athlete_NOC')
        game_data = validated_data.pop('game')
        competition_data = validated_data.pop('competition')
        medal_data = validated_data.pop('medal')

        athlete_serializer = AtletaSerializer(
            event.athlete,
            atleta_data
        )
        if athlete_serializer.is_valid(): 
            athlete_serializer.save()
        else:
            ValidationError(athlete_serializer.errors)
        
        noc_serializer = NOCSerializer(
            event.athlete_NOC,
            noc_data
        )
        if noc_serializer.is_valid(): 
            noc_serializer.save()
        else:
            ValidationError(noc_serializer.errors)

        game_serializer = OliGameSerializer(
            event.game,
            game_data
        )
        if game_serializer.is_valid(): 
            game_serializer.save()
        else:
            ValidationError(game_serializer.errors)

        competition_serializer = CompeticaoSerializer(
            event.competition,
            competition_data
        )
        if competition_serializer.is_valid(): 
            competition_serializer.save()
        else:
            ValidationError(competition_serializer.errors)
        
        medal_serializer = MedalhaSerializer(
            event.medal,
            medal_data
        )
        if medal_serializer.is_valid(): 
            medal_serializer.save()
        else:
            ValidationError(medal_serializer.errors)

        event.athlete_age = validated_data.get('athlete_age', event.athlete_age)
        event.athlete_team = validated_data.get('athlete_team', event.athlete_team)
        event.save()

        return event

