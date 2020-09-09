# Generated by Django 3.0.6 on 2020-07-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0023_auto_20200730_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pro_brand',
        ),
        migrations.AddField(
            model_name='product',
            name='pro_brand',
            field=models.ManyToManyField(null=True, to='adadmin.AddBrand'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='pro_category',
        ),
        migrations.AddField(
            model_name='product',
            name='pro_category',
            field=models.ManyToManyField(null=True, to='adadmin.AddCategory'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='pro_sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='pro_sub_category',
            field=models.ManyToManyField(null=True, to='adadmin.SubCategory'),
        ),
    ]