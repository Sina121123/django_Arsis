# Generated by Django 4.0.2 on 2022-03-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='context',
            new_name='desc',
        ),
        migrations.AddField(
            model_name='posts',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]