# Generated by Django 4.2.13 on 2025-01-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_microred_id_alter_distrito_mred_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distrito',
            name = 'mred',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='microred',
            name='codigo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
