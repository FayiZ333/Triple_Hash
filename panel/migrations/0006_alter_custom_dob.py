# Generated by Django 3.2.8 on 2021-10-12 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0005_alter_custom_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='dob',
            field=models.CharField(default=True, max_length=33, verbose_name='date of birth'),
        ),
    ]