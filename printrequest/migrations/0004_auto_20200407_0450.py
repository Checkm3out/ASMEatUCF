# Generated by Django 3.0.4 on 2020-04-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printrequest', '0003_officermodel_officertitlemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officermodel',
            name='description',
            field=models.CharField(blank=True, default='', max_length=3000),
        ),
    ]
