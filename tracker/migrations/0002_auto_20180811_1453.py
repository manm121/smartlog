# Generated by Django 2.0 on 2018-08-11 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callsubtype',
            name='request_code',
            field=models.IntegerField(),
        ),
    ]