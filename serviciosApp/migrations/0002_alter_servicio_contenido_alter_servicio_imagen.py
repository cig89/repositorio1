# Generated by Django 4.2 on 2023-04-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviciosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
    ]
