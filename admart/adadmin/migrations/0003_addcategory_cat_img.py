# Generated by Django 3.0.6 on 2020-06-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0002_auto_20200521_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcategory',
            name='cat_img',
            field=models.ImageField(default='', upload_to='product'),
        ),
    ]
