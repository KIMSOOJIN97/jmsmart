# Generated by Django 2.2.14 on 2020-07-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='comment',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='상품사진'),
        ),
    ]
