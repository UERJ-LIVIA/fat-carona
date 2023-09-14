# Generated by Django 4.2.4 on 2023-09-08 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rides', '0002_rename_saida_rides_data_saida_remove_rides_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rides',
            name='modalidade',
            field=models.CharField(choices=[('DEFAULT', 'Padrão'), ('UBER', 'Uber')], default='Modalidade.DEFAULT', max_length=12),
        ),
        migrations.AlterField(
            model_name='rides',
            name='motorista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL),
        ),
    ]
