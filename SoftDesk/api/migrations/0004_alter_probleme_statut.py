# Generated by Django 4.1.4 on 2022-12-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_projet_accessible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='probleme',
            name='statut',
            field=models.CharField(choices=[('A faire', 'A Faire'), ('En cours', 'En Cours'), ('Terminé', 'Termine')], max_length=10),
        ),
    ]
