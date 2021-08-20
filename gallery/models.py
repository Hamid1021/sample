import os
from django.dispatch import receiver
from django.db import models
from django.urls import reverse
from image_optimizer.fields import OptimizedImageField
# Create your models here.


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Gallery/{name}{ext}"
    return final_name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


class Category(models.Model):
    title = models.CharField(verbose_name="عنوان دسته", max_length=255,)
    status = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)
    slug = models.SlugField(
        verbose_name="عنوان در نوار آدرس", max_length=255, unique=True,)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته ها"


class Gallery(models.Model):
    position = models.IntegerField(
        verbose_name="موقعیت", default=0, unique=True)
    image = OptimizedImageField(verbose_name="انتخاب تصویر", upload_to=upload_image_path,
                                default="None.jpg", null=False, blank=False)
    status = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)

    alt = models.CharField(verbose_name="متن جایگزین",
                           default="بدون عنوان", max_length=255)

    categories = models.ManyToManyField(
        Category, related_name="category")

    def __str__(self):
        return f"image_{self.position}"

    def categories_active(self):
        return self.categories.filter(status=True)

    def categories_name(self):
        return ", ".join([i.title for i in self.categories_active()])

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Gallery)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Image` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Gallery)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Image` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_file = Gallery.objects.get(pk=instance.pk).image
    except Gallery.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
