# Generated by Django 4.0.3 on 2022-08-04 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perguntas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='ativo',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='pergunta',
            old_name='pergunta',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='pergunta',
            old_name='code_relacao',
            new_name='code_relation',
        ),
        migrations.RenameField(
            model_name='pergunta',
            old_name='resposta',
            new_name='question',
        ),
    ]
