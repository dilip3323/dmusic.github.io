# Generated by Django 3.0.4 on 2020-03-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.CharField(default='^C:\\Users\\dilip\\Pictures\\download.jfif', max_length=250),
        ),
    ]