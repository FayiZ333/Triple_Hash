# Generated by Django 3.2.8 on 2021-10-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0006_alter_custom_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='dob',
            field=models.CharField(max_length=33),
        ),
    ]