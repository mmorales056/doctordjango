# Generated by Django 2.2.5 on 2019-09-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorshots', '0002_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='usuario',
            field=models.CharField(max_length=45, unique=True),
        ),
    ]
