# Generated by Django 3.0.6 on 2020-07-05 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adadmin', '0017_auto_20200628_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=30, null=True)),
                ('pro_des', models.CharField(max_length=100, null=True)),
                ('pro_img', models.ImageField(default='', upload_to='products/')),
                ('pro_price', models.IntegerField(max_length=10, null=True)),
                ('pro_discount', models.IntegerField(max_length=100)),
                ('pro_size', models.CharField(blank=True, choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('2xl', '2XL')], max_length=5, null=True)),
                ('pro_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adadmin.AddBrand')),
                ('pro_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adadmin.AddCategory')),
                ('pro_sub_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adadmin.SubCategory')),
            ],
        ),
    ]