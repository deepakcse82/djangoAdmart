# Generated by Django 3.0.6 on 2020-08-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0031_auto_20200803_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_price',
            field=models.IntegerField(null=True),
        ),
    ]
