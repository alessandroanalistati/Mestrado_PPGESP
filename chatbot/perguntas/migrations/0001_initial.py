# Generated by Django 4.0.3 on 2022-05-18 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('code_user', models.CharField(max_length=15)),
                ('ativo', models.IntegerField()),
                ('code_relacao', models.CharField(max_length=15)),
                ('pergunta', models.CharField(max_length=500)),
                ('resposta', models.CharField(max_length=500)),
            ],
        ),
    ]
