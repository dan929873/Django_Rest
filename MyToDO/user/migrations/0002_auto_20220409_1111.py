# Generated by Django 3.2.12 on 2022-04-09 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='default', max_length=64),
            preserve_default=False,
        ),
    ]
