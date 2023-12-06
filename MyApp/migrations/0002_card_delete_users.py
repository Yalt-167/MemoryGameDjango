# Generated by Django 4.2.7 on 2023-12-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('paired', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
