# Generated by Django 3.1.5 on 2021-01-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]