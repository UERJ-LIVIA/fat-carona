# Generated by Django 4.2.4 on 2023-09-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_profile_gender_remove_profile_matricula_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nome',
            field=models.CharField(max_length=20),
        ),
    ]
