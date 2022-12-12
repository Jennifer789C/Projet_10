# Generated by Django 4.1.4 on 2022-12-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('balise', models.CharField(choices=[('Bug', 'Bug'), ('Amelioration', 'Amelioration'), ('Tache', 'Tache')], max_length=15)),
                ('priorite', models.CharField(choices=[('Faible', 'Faible'), ('Moyenne', 'Moyenne'), ('Elevee', 'Elevee')], max_length=10)),
                ('statut', models.CharField(choices=[('À faire', 'A Faire'), ('En cours', 'En Cours'), ('Terminé', 'Termine')], max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=2048)),
                ('type', models.CharField(choices=[('Back-end', 'Back End'), ('Front-end', 'Front End'), ('iOS', 'Ios'), ('Android', 'Android')], max_length=10)),
            ],
        ),
    ]