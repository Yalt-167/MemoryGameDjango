# Generated by Django 4.2.7 on 2023-12-04 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_userscore_users_userpassword_alter_users_useremail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='userId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='MyApp.users'),
        ),
    ]