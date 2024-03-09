# Generated by Django 5.0.2 on 2024-03-02 15:08

import phone_field.models
import users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
