# Generated by Django 4.2.2 on 2023-06-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_link', models.URLField(max_length=1000)),
                ('shortened_link', models.CharField(max_length=15)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]