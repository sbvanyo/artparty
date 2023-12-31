# Generated by Django 4.1.3 on 2023-12-31 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artpartyapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artwork',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artwork',
            old_name='collection_id',
            new_name='collection',
        ),
        migrations.RenameField(
            model_name='artwork',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='artworkartist',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='artworkartist',
            old_name='artwork_id',
            new_name='artwork',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='artwork_id',
            new_name='artwork',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
    ]