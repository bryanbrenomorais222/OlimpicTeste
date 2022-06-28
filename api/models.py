from django.db import models

class Atleta(models.Model):
    nome = models.CharField(max_length=200, blank=False, null=False)
    sex= models.CharField(max_length=2, blank=False, null=False)
    altura = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=5)
    peso = models.DecimalField(blank=True, null=True, decimal_places=1, max_digits=5)

    def __str__(self):
        return self.nome

class NOC(models.Model):
    noc = models.CharField(max_length=10, blank=True, null=True)
    regiao = models.CharField(max_length=150, blank=True, null=False)
    notas = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.noc

class Esporte(models.Model):
    nome_esporte = models.CharField(max_length=100, blank=None, null=None)

    def __str__(self):
        return self.nome_esporte

class Competicao(models.Model):
    nome_competicao = models.CharField(max_length=200, blank=None, null=None)
    esporte = models.ForeignKey('Esporte', on_delete=models.CASCADE, blank=None, null=None)

    def __str__(self):
        return self.nome_competicao

class OliGame(models.Model):
    ano = models.IntegerField(blank=None, null=None)
    sede = models.CharField(max_length=200, blank=False, null=False)
    temp = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.sede

class Medalha(models.Model):
    medal = models.CharField(max_length=50, blank=None, null=None)
    
    def __str__(self):
        return self.medal

class Evento(models.Model):
    nome_atleta = models.ForeignKey('Atleta', on_delete=models.CASCADE, blank=False,null=False)
    atleta_idade = models.IntegerField(blank=False, null=False)
    atleta_time = models.CharField(blank=False, null=False, max_length=100)
    atleta_noc = models.ForeignKey('NOC', on_delete=models.CASCADE, blank=False, null=False)
    olimpic_game = models.ForeignKey('OliGame', on_delete=models.CASCADE, blank=False, null=False)
    competicao_nome = models.ForeignKey('Competicao', on_delete=models.CASCADE, blank=False, null=False)
    tipo_medalha = models.ForeignKey('Medalha', on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.nome_atleta} - {self.atleta_noc} - {self.tipo_medalha}'