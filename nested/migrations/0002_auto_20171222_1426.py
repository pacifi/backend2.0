# Generated by Django 2.0 on 2017-12-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nested', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='num_starts',
        ),
        migrations.AddField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musician',
            name='instrument',
            field=models.CharField(max_length=100),
        ),
    ]
