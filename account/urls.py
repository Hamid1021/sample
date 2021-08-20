"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from account.views import (
    ArticleList, ArticleCreate, ArticleUpdate, ArticleDelete, CategoryList, CategoryCreate,
    CategoryUpdate, CategoryDelete, CommentList, CommentUpdate, CommentDelete,
    CategoryGalleryList, CategoryGalleryCreate, CategoryGalleryUpdate, CategoryGalleryDelete,
    GalleryList, GalleryCreate, GalleryUpdate, GalleryDelete, GalleryHomeList,
    GalleryHomeCreate, GalleryHomeUpdate, GalleryHomeDelete, ContactList,
    ContactUpdate, ContactDelete, UserList, UserCreate, UserUpdate, UserDelete,
    SeoInformationList, SeoInformationCreate, SeoInformationUpdate, SeoInformationDelete,
    SiteMapList, SiteMapUpdate



)
from django.contrib.auth import views
app_name = 'admin_account'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # ////////////////////////////////////////////////// Blog ///////////////////////////////////////////////////////////////
    # //////////////////////////////////// Article ///////////////////////////////////////////
    path("account/", ArticleList.as_view(), name="home"),
    path("account/article-create/", ArticleCreate.as_view(), name="article_create"),
    path("account/article-update/<int:pk>/",
         ArticleUpdate.as_view(), name="article_update"),
    path("account/article-delete/<int:pk>/",
         ArticleDelete.as_view(), name="article_delete"),
    # //////////////////////////////////// Category ///////////////////////////////////////////
    path("account/category/", CategoryList.as_view(), name="home_category"),
    path("account/category-create/",
         CategoryCreate.as_view(), name="category_create"),
    path("account/category-update/<int:pk>/",
         CategoryUpdate.as_view(), name="category_update"),
    path("account/category-delete/<int:pk>/",
         CategoryDelete.as_view(), name="category_delete"),
    # //////////////////////////////////// Comment ///////////////////////////////////////////
    path("account/comment/", CommentList.as_view(), name="home_comment"),
    path("account/comment-update/<int:pk>/",
         CommentUpdate.as_view(), name="comment_update"),
    path("account/comment-delete/<int:pk>/",
         CommentDelete.as_view(), name="comment_delete"),
    # ////////////////////////////////////////////////// Gallery ///////////////////////////////////////////////////////////////
    # //////////////////////////////////// Category ///////////////////////////////////////////
    path("account/gallery-category/", CategoryGalleryList.as_view(),
         name="home_category_gallery"),
    path("account/gallery-category-create/",
         CategoryGalleryCreate.as_view(), name="category_create_gallery"),
    path("account/gallery-category-update/<int:pk>/",
         CategoryGalleryUpdate.as_view(), name="category_update_gallery"),
    path("account/gallery-category-delete/<int:pk>/",
         CategoryGalleryDelete.as_view(), name="category_delete_gallery"),
    # //////////////////////////////////// Picture ///////////////////////////////////////////
    path("account/gallery/", GalleryList.as_view(), name="home_gallery"),
    path("account/gallery-create/",
         GalleryCreate.as_view(), name="create_gallery"),
    path("account/gallery-update/<int:pk>/",
         GalleryUpdate.as_view(), name="update_gallery"),
    path("account/gallery-delete/<int:pk>/",
         GalleryDelete.as_view(), name="delete_gallery"),
    # //////////////////////////////////// Gallery_Home ///////////////////////////////////////////
    path("account/gallery_home/", GalleryHomeList.as_view(),
         name="home_gallery_home"),
    path("account/gallery_home-create/",
         GalleryHomeCreate.as_view(), name="create_gallery_home"),
    path("account/gallery_home-update/<int:pk>/",
         GalleryHomeUpdate.as_view(), name="update_gallery_home"),
    path("account/gallery_home-delete/<int:pk>/",
         GalleryHomeDelete.as_view(), name="delete_gallery_home"),
    # //////////////////////////////////// Contact ///////////////////////////////////////////
    path("account/contact/", ContactList.as_view(),
         name="home_contact"),
    path("account/contact-update/<int:pk>/",
         ContactUpdate.as_view(), name="update_contact"),
    path("account/contact-delete/<int:pk>/",
         ContactDelete.as_view(), name="delete_contact"),
    # //////////////////////////////////// User ///////////////////////////////////////////
    path("account/user/", UserList.as_view(),
         name="home_user"),
    path("account/user-create/",
         UserCreate.as_view(), name="create_user"),
    path("account/user-update/<int:pk>/",
         UserUpdate.as_view(), name="update_user"),
    path("account/user-delete/<int:pk>/",
         UserDelete.as_view(), name="delete_user"),
    # //////////////////////////////////// SeoInformation ///////////////////////////////////////////
    path("account/seo/", SeoInformationList.as_view(),
         name="home_seo"),
    path("account/seo-create/",
         SeoInformationCreate.as_view(), name="create_seo"),
    path("account/seo-update/<int:pk>/",
         SeoInformationUpdate.as_view(), name="update_seo"),
    path("account/seo-delete/<int:pk>/",
         SeoInformationDelete.as_view(), name="delete_seo"),
    # //////////////////////////////////// SiteMap ///////////////////////////////////////////
    path("account/sitemap/", SiteMapList.as_view(),
         name="home_sitemap"),
    path("account/sitemap-update/<int:pk>/",
         SiteMapUpdate.as_view(), name="update_sitemap"),
]
