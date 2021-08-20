from django.contrib.sites.models import Site
from django.shortcuts import render
from seo.models import Seo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from blog.models import Article, Category, Comment
from gallery.models import Category as GalleryCategory, Gallery
from home_gallery.models import Gallery_Home
from cantact.models import Message
from django.urls import reverse_lazy
from account.mixins import ValidateFormMixin, ValidFormMixin, ValidFormCreateMixin
from django.contrib.auth import get_user_model

User = get_user_model()
# //////////////////////////////////////////////////////// Blog ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// Article /////////////////////////////////////////////


class ArticleList(LoginRequiredMixin, ListView):
    queryset = Article.objects.all()
    template_name = "Blog/Article/content_admin_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    fields = ["title", "slug", "keyword", "category",
              "description", "thumbnail", "status", ]
    model = Article
    template_name = "Blog/Article/content_admin_article_create_update.html"
    success_url = reverse_lazy("admin_account:home")


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    fields = ["title", "slug", "keyword", "category",
              "description", "thumbnail", "status", ]
    model = Article
    template_name = "Blog/Article/content_admin_article_create_update.html"
    success_url = reverse_lazy("admin_account:home")


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "Blog/Article/content_admin_article.html"
    success_url = reverse_lazy("admin_account:home")

# ///////////////////////////////////////// Category /////////////////////////////////////////////


class CategoryList(LoginRequiredMixin, ListView):
    queryset = Category.objects.all()
    template_name = "Blog/Category/content_admin_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class CategoryCreate(LoginRequiredMixin, CreateView):
    fields = ["title", "slug", "status", ]
    model = Category
    template_name = "Blog/Category/content_admin_category_create_update.html"
    success_url = reverse_lazy("admin_account:home_category")


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    fields = ["title", "slug", "status", ]
    model = Category
    template_name = "Blog/Category/content_admin_category_create_update.html"
    success_url = reverse_lazy("admin_account:home_category")


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "Blog/Category/content_admin_category.html"
    success_url = reverse_lazy("admin_account:home_category")
# ///////////////////////////////////////// Keyword /////////////////////////////////////////////


class CommentList(LoginRequiredMixin, ListView):
    queryset = Comment.objects.all()
    template_name = "Blog/Comment/content_admin_comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class CommentUpdate(LoginRequiredMixin, UpdateView):
    fields = ["fullname", "email", "message", "status", ]
    model = Comment
    template_name = "Blog/Comment/content_admin_comment_update.html"
    success_url = reverse_lazy("admin_account:home_comment")


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = "Blog/Comment/content_admin_comment.html"
    success_url = reverse_lazy("admin_account:home_comment")

# //////////////////////////////////////////////////////// Gallery ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// Category /////////////////////////////////////////////


class CategoryGalleryList(LoginRequiredMixin, ListView):
    queryset = GalleryCategory.objects.all()
    template_name = "Gallery/Category/content_admin_category_gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class CategoryGalleryCreate(LoginRequiredMixin, CreateView):
    fields = ["title", "slug", "status", ]
    model = GalleryCategory
    template_name = "Gallery/Category/content_admin_category_gallery_create_update.html"
    success_url = reverse_lazy("admin_account:home_category_gallery")


class CategoryGalleryUpdate(LoginRequiredMixin, UpdateView):
    fields = ["title", "slug", "status", ]
    model = GalleryCategory
    template_name = "Gallery/Category/content_admin_category_gallery_create_update.html"
    success_url = reverse_lazy("admin_account:home_category_gallery")


class CategoryGalleryDelete(LoginRequiredMixin, DeleteView):
    model = GalleryCategory
    template_name = "Gallery/Category/content_admin_category_gallery.html"
    success_url = reverse_lazy("admin_account:home_category_gallery")

# ///////////////////////////////////////// Gallery /////////////////////////////////////////////


class GalleryList(LoginRequiredMixin, ListView):
    queryset = Gallery.objects.all()
    template_name = "Gallery/Picture/content_admin_gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class GalleryCreate(LoginRequiredMixin, CreateView):
    fields = [
        "position", "image", "status", "alt", "categories",
    ]
    model = Gallery
    template_name = "Gallery/Picture/content_admin_gallery_create_update.html"
    success_url = reverse_lazy("admin_account:home_gallery")


class GalleryUpdate(LoginRequiredMixin, UpdateView):
    fields = [
        "position", "image", "status", "alt", "categories",
    ]
    model = Gallery
    template_name = "Gallery/Picture/content_admin_gallery_create_update.html"
    success_url = reverse_lazy("admin_account:home_gallery")


class GalleryDelete(LoginRequiredMixin, DeleteView):
    model = Gallery
    template_name = "Gallery/Picture/content_admin_gallery.html"
    success_url = reverse_lazy("admin_account:home_gallery")

# //////////////////////////////////////////////////////// GalleryHome ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// GalleryHome /////////////////////////////////////////////


class GalleryHomeList(LoginRequiredMixin, ListView):
    queryset = Gallery_Home.objects.all()
    template_name = "GalleryHome/content_admin_gallery_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class GalleryHomeCreate(LoginRequiredMixin, CreateView):
    fields = ["position", "image", "status", ]
    model = Gallery_Home
    template_name = "GalleryHome/content_admin_gallery_home_create_update.html"
    success_url = reverse_lazy("admin_account:home_gallery_home")


class GalleryHomeUpdate(LoginRequiredMixin, UpdateView):
    fields = ["position", "image", "status", ]
    model = Gallery_Home
    template_name = "GalleryHome/content_admin_gallery_home_create_update.html"
    success_url = reverse_lazy("admin_account:home_gallery_home")


class GalleryHomeDelete(LoginRequiredMixin, DeleteView):
    model = Gallery_Home
    template_name = "GalleryHome/content_admin_gallery_home.html"
    success_url = reverse_lazy("admin_account:home_gallery_home")

# //////////////////////////////////////////////////////// Contact ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// Contact /////////////////////////////////////////////


class ContactList(LoginRequiredMixin, ListView):
    queryset = Message.objects.all()
    template_name = "Contact/content_admin_contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class ContactUpdate(LoginRequiredMixin, ValidateFormMixin, UpdateView):
    fields = ["full_name", "email", "subject", "message", "status", ]
    model = Message
    template_name = "Contact/content_admin_contact_update.html"
    success_url = reverse_lazy("admin_account:home_contact")


class ContactDelete(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "Contact/content_admin_contact.html"
    success_url = reverse_lazy("admin_account:home_contact")

# //////////////////////////////////////////////////////// User ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// User /////////////////////////////////////////////


class UserList(LoginRequiredMixin, ListView):
    queryset = User.objects.all()
    template_name = "User/content_admin_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class UserCreate(LoginRequiredMixin, ValidFormCreateMixin, CreateView):
    fields = [
        "username", "first_name", "last_name", "gender",
        "email", "image", "phone_number", "is_active", "is_staff",
        "is_superuser", "user_permissions", "password", "pass_per_save",
    ]
    model = User
    template_name = "User/content_admin_user_create_update.html"
    success_url = reverse_lazy("admin_account:home_user")


class UserUpdate(LoginRequiredMixin, ValidFormMixin, UpdateView):
    fields = [
        "username", "first_name", "last_name", "gender",
        "email", "image", "phone_number", "is_active", "is_staff",
        "is_superuser", "user_permissions", "password", "pass_per_save",
    ]
    model = User
    template_name = "User/content_admin_user_create_update.html"
    success_url = reverse_lazy("admin_account:home_user")


class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "User/content_admin_user.html"
    success_url = reverse_lazy("admin_account:home_user")

# //////////////////////////////////////////////////////// Seo ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// SeoInformation /////////////////////////////////////////////


class SeoInformationList(LoginRequiredMixin, ListView):
    queryset = Seo.objects.all()
    template_name = "SeoInformation/content_admin_seo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class SeoInformationCreate(LoginRequiredMixin, CreateView):
    fields = [
        "site_name", "description", "status", "image_logo", "owner", "telegram",
        "telegram_1", "instagram", "instagram_1", "phone_number", "phone_number_1",
        "phone_number_2", "phone_number_3", "phone", "phone_1",
        "phone_2", "phone_3", "url", "kyword", "address", "time_work_start",
        "time_work_end", "addres_google_map", "email", "email_1",
    ]
    model = Seo
    template_name = "SeoInformation/content_admin_seo_create_update.html"
    success_url = reverse_lazy("admin_account:home_seo")


class SeoInformationUpdate(LoginRequiredMixin, UpdateView):
    fields = [
        "site_name", "description", "status", "image_logo", "owner", "telegram",
        "telegram_1", "instagram", "instagram_1", "phone_number", "phone_number_1",
        "phone_number_2", "phone_number_3", "phone", "phone_1",
        "phone_2", "phone_3", "url", "kyword", "address", "time_work_start",
        "time_work_end", "addres_google_map", "email", "email_1",
    ]
    model = Seo
    template_name = "SeoInformation/content_admin_seo_create_update.html"
    success_url = reverse_lazy("admin_account:home_seo")


class SeoInformationDelete(LoginRequiredMixin, DeleteView):
    model = Seo
    template_name = "SeoInformation/content_admin_seo.html"
    success_url = reverse_lazy("admin_account:home_seo")

# //////////////////////////////////////////////////////// SiteMap ///////////////////////////////////////////////////////////
# ///////////////////////////////////////// SiteMap /////////////////////////////////////////////


class SiteMapList(LoginRequiredMixin, ListView):
    queryset = Site.objects.all()
    template_name = "SiteMap/content_admin_sitemap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seo_information = Seo.objects.all().filter(status=True).last()
        context["seo_object"] = seo_information
        return context


class SiteMapUpdate(LoginRequiredMixin, UpdateView):
    fields = ["id", "domain", "name", ]
    model = Site
    template_name = "SiteMap/content_admin_sitemap_update.html"
    success_url = reverse_lazy("admin_account:home_sitemap")
