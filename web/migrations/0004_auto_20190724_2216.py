# Generated by Django 2.2.3 on 2019-07-24 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190724_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(),
        ),
    ]