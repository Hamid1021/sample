from django.db import models
from extensions.utils import jalali_converter
from image_optimizer.fields import OptimizedImageField
from django.dispatch import receiver
import os
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"Blog/{name}{ext}"
    return final_name


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(unique=True, max_length=100,
                            verbose_name="آدرس دسته بندی")
    status = models.BooleanField(verbose_name="فعال / غیر فعال", default=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Article(models.Model):
    STATUS_CHOICES = (
        ("d", "پیش‌نویس"),
        ("p", "منتشر شده"),
    )
    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(unique=True, max_length=255,
                            verbose_name="آدرس مقاله")
    keyword = models.CharField(
        max_length=255, verbose_name="کلید واژه", default="")
    category = models.ManyToManyField(
        Category, verbose_name="دسته بندی", related_name="categories", blank=True)
    description = RichTextUploadingField(verbose_name="توضیحات")
    thumbnail = OptimizedImageField(
        blank=True, upload_to=upload_image_path,
        default="None.jpg", verbose_name="انتخاب تصویر")
    publish = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان انتشار")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار", default="d")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:article", kwargs={"pk": self.pk, "slug": self.slug})

    def categories_name(self):
        return "،\n".join([i.title for i in self.category_published()])

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    objects = ArticleManager()


class CommentManager(models.Manager):
    def get_object_or_None(self, article):
        try:
            obj = self.get_queryset().filter(article=article, status=True)
        except:
            obj = None
        return obj

    def get_count(self, article):
        try:
            obj = self.get_queryset().filter(article=article, status=True).count
        except:
            obj = None
        return obj


class Comment(models.Model):
    fullname = models.CharField(
        verbose_name="نام شما", max_length=255, blank=True, null=True, default="بدون نام")
    email = models.CharField(verbose_name="آدرس ایمیل شما",
                             max_length=255, blank=True, null=True)
    message = models.TextField(
        verbose_name="پیام شما", blank=False, null=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ارسال به میلادی")
    status = models.BooleanField(
        verbose_name="نمایش/عدم نمایش", blank=False, null=False, default=False)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, verbose_name="برای مقاله ی")

    objects = CommentManager()

    def __str__(self):
        return f"{self.article.title}"

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "زمان ارسال به شمسی"

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ['-created']


@receiver(models.signals.post_delete, sender=Article)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes thumbnail from filesystem
    when corresponding `thumbnail` object is deleted.
    """
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)


@receiver(models.signals.pre_save, sender=Article)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old thumbnail from filesystem
    when corresponding `thumbnail` object is updated
    with new thumbnail.
    """
    if not instance.pk:
        return False

    try:
        old_file = Article.objects.get(pk=instance.pk).thumbnail
    except Article.DoesNotExist:
        return False

    new_file = instance.thumbnail
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
