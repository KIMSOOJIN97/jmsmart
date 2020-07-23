# Generated by Django 3.0.8 on 2020-07-22 09:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('content', models.TextField(default='', verbose_name='내용')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='날짜')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.Seller')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
    ]