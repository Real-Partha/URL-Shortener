# Generated by Django 4.2.2 on 2023-06-29 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0002_url_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='count',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
