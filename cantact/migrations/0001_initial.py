# Generated by Django 3.2.5 on 2021-08-17 11:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='بی نام', max_length=255, null=True, verbose_name='نام ارسال کننده')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='آدرس ایمیل')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='موضوع پیام')),
                ('message', models.TextField(blank=True, max_length=255, null=True, verbose_name='پیام شما')),
                ('status', models.CharField(choices=[('r', 'خوانده شده'), ('u', 'خوانده نشده')], default='u', help_text='لطفا بعد از اتمام مطالعه بر روی ذخیره کلیک نمایید تا پیام به صورت خوانده شده تغییر وضعیت بدهد', max_length=1, verbose_name='وضعیت')),
                ('send_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان ارسال به میلادی')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'ordering': ['-status'],
            },
        ),
    ]
