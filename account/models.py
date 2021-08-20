from django.dispatch import receiver
import os
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import date
import uuid
from django.apps import apps
from django.contrib.auth.hashers import make_password

from random import randint
from django.utils import timezone
from image_optimizer.fields import OptimizedImageField


class CustomUserManager(UserManager):
    @classmethod
    def check_full_int(self, phone_number):
        phone = phone_number
        try:
            phone = int(phone)
            return False
        except:
            return True

    @classmethod
    def checking_phone_number(cls, phone_number):
        """
        checking phone number the phone_number checking contains 0 and 9 in the start.
        """
        phone_number = phone_number or ''

        if phone_number[0] != "0":
            return 0
        elif phone_number[1] != "9":
            return 1
        elif len(phone_number) > 11:
            return 2
        elif cls.check_full_int(phone_number):
            return 3
        else:
            return phone_number

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')

        phone_number_status = self.checking_phone_number(
            extra_fields["phone_number"])

        if phone_number_status == 0:
            raise ValueError('The given phone_number must start with 0')
        elif phone_number_status == 1:
            raise ValueError(
                'The given phone_number index 1 must start with 9')
        elif phone_number_status == 2:
            raise ValueError('The given phone_number character must be 11')
        elif phone_number_status == 3:
            raise ValueError(
                'The given phone_number character must be integer')

        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(
            username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def generate_ranint(self):
        return randint(100000, 999999)

    def create_user(self, username, email=None, password=None, ** extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        # str(uuid.uuid4())[-1:8:-1] is a 24 random character
        extra_fields.setdefault('custom_user_id', str(uuid.uuid4())[:11:-1])
        extra_fields.setdefault('gender', "m")
        extra_fields.setdefault('pass_per_save', password or None)
        extra_fields.setdefault('code_send', self.generate_ranint())
        extra_fields.setdefault('email_sended', False)
        return self._create_user(username, email, password, **extra_fields)

    def _create_super_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name)
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('custom_user_id', str(uuid.uuid4())[:11:-1])
        extra_fields.setdefault('gender', "m")
        extra_fields.setdefault('pass_per_save', password or None)
        extra_fields.setdefault('code_send', self.generate_ranint())
        extra_fields.setdefault('email_sended', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_super_user(username, email, password, **extra_fields)


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Profile/{name}{ext}"
    return final_name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


class User(AbstractUser):
    GENDER_CHOICES = (
        ("m", "مرد"),
        ("w", "زن"),
        ("b", "ترجیح می دهم نگویم"),
    )
    image = OptimizedImageField(
        upload_to=upload_image_path,
        optimized_image_output_size=(540, 540),
        optimized_image_resize_method='thumbnail'  # 'thumbnail', 'cover' or None
        , null=True, blank=True, verbose_name="تصویر پروفایل", default="None.jpg")
    pass_per_save = models.CharField(
        verbose_name="گذر واژه هش نشده", max_length=255, blank=True)
    gender = models.CharField(
        verbose_name="جنسیت", max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    phone_number = models.CharField(
        verbose_name="شماره همراه", max_length=11, null=True, blank=True, unique=True)
    custom_user_id = models.CharField(
        verbose_name="کد اختصاصی کاربر", max_length=24, null=True, blank=True, unique=True)
    code_send = models.IntegerField(
        verbose_name="کد ارسال شده", null=True, blank=True)
    email_sended = models.BooleanField(
        default=False, verbose_name="ایمیل ارسال شده است")

    objects = CustomUserManager()


# These two auto-delete files from filesystem when they are unneeded:


@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `User` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `User` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).image
    except User.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
