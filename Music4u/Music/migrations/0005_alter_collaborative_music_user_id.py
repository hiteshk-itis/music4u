# Generated by Django 4.1.3 on 2022-12-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0004_alter_collaborative_music_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborative_music',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
