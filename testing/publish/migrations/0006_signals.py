# Generated by Django 4.1.1 on 2022-09-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0005_album_track_remove_catdog_cat_remove_catdog_dog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
