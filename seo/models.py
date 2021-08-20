from django.contrib.sites.models import Site
from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import NullBooleanField
from image_optimizer.fields import OptimizedImageField
import os
# Create your models here.


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Logo/{name}{ext}"
    return final_name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def get_url(model):
    try:
        text = f"http://{model.objects.all().last().domain}"
    except:
        text = ""
    return text


class Seo(models.Model):
    site_name = models.CharField(
        verbose_name="نام سایت", max_length=255, blank=True, null=True, default="وبلاگ")
    status = models.BooleanField(default=False, verbose_name="فعال/غیر فعال")
    image_logo = OptimizedImageField(verbose_name="انتخاب تصویر لوگو", upload_to=upload_image_path,
                                     default="None.jpg", null=True, blank=True)
    owner = models.CharField(verbose_name="مالک سایت",
                             max_length=255, null=True, blank=True)
    telegram = models.CharField(
        verbose_name="آدرس کانال", max_length=255, blank=True, null=True)
    telegram_1 = models.CharField(
        verbose_name="آدرس کانال_1", max_length=255, blank=True, null=True)
    instagram = models.CharField(
        verbose_name="صفحه ایستا گرام", max_length=255, blank=True, null=True)
    instagram_1 = models.CharField(
        verbose_name="صفحه ایستا گرام_1", max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        verbose_name="شماره همراه", max_length=11, blank=True, null=True)
    phone_number_1 = models.CharField(
        verbose_name="شماره همراه_1", max_length=11, blank=True, null=True)
    phone_number_2 = models.CharField(
        verbose_name="شماره همراه_2", max_length=11, blank=True, null=True)
    phone_number_3 = models.CharField(
        verbose_name="شماره همراه_3", max_length=11, blank=True, null=True)
    phone = models.CharField(verbose_name="شماره تلفن",
                             max_length=11, blank=True, null=True)
    phone_1 = models.CharField(verbose_name="شماره تلفن_1",
                               max_length=11, blank=True, null=True)
    phone_2 = models.CharField(verbose_name="شماره تلفن_2",
                               max_length=11, blank=True, null=True)
    phone_3 = models.CharField(verbose_name="شماره تلفن_3",
                               max_length=11, blank=True, null=True)
    url = models.URLField(verbose_name="آدرس دامنه سایت",
                          max_length=255, blank=True, null=True, default=get_url(Site))
    kyword = models.TextField(
        verbose_name="کلید واژه ها", blank=True, null=True)
    description = models.TextField(
        verbose_name="درباره سایت", blank=True, null=True)
    addres_google_map = models.TextField(
        verbose_name="آدرس در گوگل مپ", blank=True, null=True)
    time_work_start = models.TimeField(verbose_name="ساعت شروع کار",
                                       blank=True, null=True)
    time_work_end = models.TimeField(verbose_name="ساعت پایان کار",
                                     blank=True, null=True)
    address = models.TextField(
        verbose_name="آدرس", blank=True, null=True)
    email = models.EmailField(verbose_name="آدرس ایمیل", blank=True, null=True)
    email_1 = models.EmailField(
        verbose_name="آدرس ایمیل_1", blank=True, null=True)

    class Meta:
        verbose_name = "سئو"
        verbose_name_plural = "سئو"

    def __str__(self):
        return f"{self.site_name}"
