# Generated by Django 5.1.3 on 2024-11-19 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Turmas',
            new_name='Turma',
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('data', models.DateField(verbose_name='Data de aplicação')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso', verbose_name='Curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.disciplina', verbose_name='Disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pessoa', verbose_name='Pessoa')),
            ],
        ),
    ]
