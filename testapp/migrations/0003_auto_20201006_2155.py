# Generated by Django 3.1.2 on 2020-10-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20201006_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_model',
            name='images',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
