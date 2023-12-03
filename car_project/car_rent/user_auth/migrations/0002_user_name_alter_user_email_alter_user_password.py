# Generated by Django 4.2.7 on 2023-12-03 15:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='Name must be more than 3 char'), django.core.validators.RegexValidator(message='Name accepts alphabets only', regex='^[a-zA-Z]+(\\s[a-zA-Z]+)?$')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(limit_value=6, message='Password must be between 6 to 15 char')]),
        ),
    ]
