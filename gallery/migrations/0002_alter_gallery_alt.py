# Generated by Django 3.2.5 on 2021-08-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='alt',
            field=models.CharField(default='بدون عنوان', max_length=255, verbose_name='متن جایگزین'),
        ),
    ]
