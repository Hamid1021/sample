from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter


class Message(models.Model):
    STATUS_CHOICES = (
        ("r", "خوانده شده"),
        ("u", "خوانده نشده"),
    )
    full_name = models.CharField(verbose_name="نام ارسال کننده", blank=True, null=True, max_length=255, default="بی نام")
    email = models.EmailField(verbose_name="آدرس ایمیل", blank=True, null=True, max_length=255)
    subject = models.CharField(verbose_name="موضوع پیام", blank=True, null=True, max_length=255)
    message = models.TextField(verbose_name="پیام شما", blank=False, null=False, default="", max_length=255)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت", default="u", help_text="لطفا بعد از اتمام مطالعه بر روی ذخیره کلیک نمایید تا پیام به صورت خوانده شده تغییر وضعیت بدهد")
    send_time = models.DateTimeField(
        default=timezone.now, verbose_name="زمان ارسال به میلادی")
        
    def __str__(self):
        return f"{self.full_name}"
        
    def jsend_time(self):
        return jalali_converter(self.send_time)
    jsend_time.short_description = "زمان ارسال به شمسی"
        
    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"
        ordering = ["-status"]