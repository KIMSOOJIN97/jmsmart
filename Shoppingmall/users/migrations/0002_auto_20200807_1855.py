# Generated by Django 3.0.8 on 2020-08-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='item_count',
            field=models.IntegerField(verbose_name='상품수'),
        ),
    ]
