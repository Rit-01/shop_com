# Generated by Django 3.1 on 2021-03-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210315_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
