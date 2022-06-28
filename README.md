# OlimpicTeste

# Instalation 
Crie um ambiente virtual, clone esse repositório e instale as dependências necessárias:

python3 -m venv venv
source ./venv/Scripts/activate
git clone https://github.com/bryanbrenomorais222/OlimpicTeste.git

Inicialize a database
python manage.py migrate

Importe o dataset 
python manage.py import_noc dataset/noc_regions.csv
python manage.py import_events dataset/athlete_events.csv

# Uso
A implementação desta API, possui todos os métodos básicos Http.

