# Generated by Django 4.1.6 on 2023-03-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user36198', max_length=30),
        ),
    ]
