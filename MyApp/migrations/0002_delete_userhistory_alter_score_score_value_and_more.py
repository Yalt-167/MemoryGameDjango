# Generated by Django 4.2.7 on 2023-12-08 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserHistory',
        ),
        migrations.AlterField(
            model_name='score',
            name='score_value',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]