from django.core.management.base import BaseCommand, CommandError
from api.models import NOC
from csv import reader

class Command(BaseCommand):
    help = 'Import NOCs from .csv file'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, help='The .csv filename containing the NOC information')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        try:
            with open(filename) as file:
                r = reader(file)
                for row in r:
                    noc, regiao, notas = row
                    if noc == 'NOC': continue

                    if noc == 'SIN': noc = 'SGP' 

                    obj, created= NOC.objects.get_or_create(
                        noc=noc,
                        regiao=regiao,
                        notas=notas
                        )
                    if created: 
                        obj.save()
                        print(f'{obj} saved!')
                    else:
                        print(f'{obj} already saved!')
        except FileNotFoundError as e:
            print("Deu erro, agora lascou!"+e)
        
        