# Generated by Django 3.1.4 on 2021-01-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0004_auto_20210120_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=204, unique=True),
        ),
    ]
