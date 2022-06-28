# Generated by Django 3.1.5 on 2021-01-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=1)),
                ('height', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
            ],
            options={
                'verbose_name': 'Athlete',
                'verbose_name_plural': 'Athletes',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('season', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='NOC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noc', models.CharField(max_length=3)),
                ('region', models.CharField(max_length=30)),
                ('notes', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'NOC',
                'verbose_name_plural': 'NOCs',
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Sport',
                'verbose_name_plural': 'Sports',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_age', models.IntegerField(null=True)),
                ('athlete_team', models.CharField(max_length=30)),
                ('event', models.CharField(max_length=200)),
                ('medal', models.CharField(max_length=7)),
                ('athlete', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='api.athlete')),
                ('athlete_NOC', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='api.noc')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='api.game')),
                ('sport', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='api.sport')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
    ]
