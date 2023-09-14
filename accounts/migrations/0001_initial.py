# Generated by Django 4.2 on 2023-06-16 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('idade', models.IntegerField(max_length=3)),
                ('email', models.EmailField(max_length=50)),
                ('matricula', models.IntegerField(max_length=20)),
                ('gender', models.CharField(choices=[('Masculino', 'Opcao 1'), ('Feminino', 'Opcao 2')], default='Opcao_1', max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
