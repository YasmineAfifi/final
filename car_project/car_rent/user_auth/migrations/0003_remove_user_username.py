# Generated by Django 4.2.7 on 2023-12-03 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_user_name_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
