# Generated by Django 3.0.8 on 2020-08-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0028_auto_20200819_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='target',
            field=models.CharField(max_length=50),
        ),
    ]