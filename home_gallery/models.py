from django.db import models
from django.dispatch import receiver
import os
from image_optimizer.fields import OptimizedImageField

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Gallery_Home/{name}{ext}"
    return final_name


class Gallery_Home(models.Model):
    position = models.IntegerField(
        verbose_name="موقعیت", default=0, unique=True)
    image = OptimizedImageField(
        verbose_name="انتخاب تصویر", upload_to=upload_image_path,
        default="None.jpg", null=False, blank=False)
    status = models.BooleanField(verbose_name="فعال/غیرفعال", default=True)

    def __str__(self):
        return f"image_{self.position}"

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "گالری صفحه اصلی"


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Gallery_Home)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes image from filesystem
    when corresponding `Gallery_Home` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=Gallery_Home)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old image from filesystem
    when corresponding `Gallery_Home` object is updated
    with new image.
    """
    if not instance.pk:
        return False

    try:
        old_file = Gallery_Home.objects.get(pk=instance.pk).image
    except Gallery_Home.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
