# Generated by Django 3.0.6 on 2020-07-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0021_product_pro_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_size',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
