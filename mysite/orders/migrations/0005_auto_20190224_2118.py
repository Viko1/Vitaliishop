# Generated by Django 2.1.5 on 2019-02-24 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190223_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products in order'},
        ),
    ]
