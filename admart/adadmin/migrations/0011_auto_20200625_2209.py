# Generated by Django 3.0.6 on 2020-06-25 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0010_auto_20200625_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_cat_name',
            new_name='sub_cat_names',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_cat_types',
            new_name='sub_cat_type',
        ),
    ]
