# Generated by Django 5.0.1 on 2024-01-28 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('univ', '0007_alter_etudiant_filiere_alter_etudiant_parcours_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='etudiant',
            options={'verbose_name': 'etudiant', 'verbose_name_plural': 'etudiants'},
        ),
    ]
