# Generated by Django 4.2.13 on 2025-01-18 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_microred_codigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='establecimiento',
            old_name='microred',
            new_name='nmred',
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('codigo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('mred', models.CharField(blank=True, max_length=6, null=True)),
                ('dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.departamento')),
                ('prov', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.provincia')),
                ('red', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.red')),
            ],
        ),
        migrations.AddField(
            model_name='establecimiento',
            name='dist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.distrito'),
        ),
    ]
