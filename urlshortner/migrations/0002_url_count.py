# Generated by Django 4.2.2 on 2023-06-29 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]