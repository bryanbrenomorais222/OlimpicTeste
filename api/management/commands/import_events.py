from django.core.management.base import BaseCommand, CommandError
from api.models import Atleta,Evento, OliGame, Esporte, Competicao, Medalha, NOC
from csv import reader


class Command(BaseCommand):
    help = 'Import Events from .csv file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The .csv filenome containing the noc information')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        events = Evento.objects.select_related(
        'atleta',
        'atleta_NOC',
        'game',
        'competicao',
        'medal'
    )
        
        atletas = Atleta.objects.all()
        olimpic_games = OliGame.objects.all()
        nome_esportes = Esporte.objects.all()
        competicao_nomes = Competicao.objects.select_related('nome_esporte')
        tipo_medalhas= Medalha.objects.all()
        nocs = NOC.objects.all()
        try:
            with open(filename) as file:
                r = reader(file)
                for n, row in enumerate(r):
                    pk, name,sex, idade, peso, altura, atleta_time, noc, olimpic_game, ano, temp, sede, nome_esporte, competicao_nome, tipo_medalha = row
                    if pk == 'ID': continue
                    
                    atleta, created = atletas.get_or_create(
                        pk=pk,
                        name=name,
                        sex=sex,
                        altura=round(float(altura), 1) if altura != 'NA' else None,
                        peso=round(float(peso), 1) if peso != 'NA' else None,
                        )
                    if created: atleta.save()

                    noc = nocs.get(noc=noc)

                    olimpic_game, created = olimpic_games.get_or_create(
                        ano=ano,
                        temp=temp,
                        sede=sede
                        )
                    if created: olimpic_game.save()

                    nome_esporte, created = nome_esportes.get_or_create(nome=nome_esporte)
                    if created: nome_esporte.save()

                    competicao_nome, created = competicao_nomes.get_or_create(
                        nome=competicao_nome,
                        nome_esporte=nome_esporte
                        )
                    if created: competicao_nome.save()

                    tipo_medalha, created = tipo_medalhas.get_or_create(nome=tipo_medalha)
                    if created: tipo_medalha.save()
                    
                    event, created = events.get_or_create(
                        name=name,
                        atleta_idade=idade if idade != 'NA' else None,
                        atleta_time=atleta_time,
                        noc=noc,
                        olimpic_game=olimpic_game,
                        competicao_nome=competicao_nome,
                        tipo_medalha=tipo_medalha
                    )
                    if created: 
                        event.save()
                        print(f'Event {n} saved!')
                    else:
                        print(f'Event {n} already saved!')
        except FileNotFoundError as e:
            raise CommandError(e)
        