# Generated by Django 2.1.4 on 2019-05-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_client', '0002_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact',
            field=models.IntegerField(),
        ),
    ]