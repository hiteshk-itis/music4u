# Generated by Django 4.1.3 on 2022-12-01 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0002_alter_collaborative_music_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborative_music',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
