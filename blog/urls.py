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
from blog.views import blog_page, load_more, article_page, load_more_2


app_name = 'blog'

urlpatterns = [
    path("blog/", blog_page, name="blog"),
    path("blog/<int:pk>/<slug:slug>/", article_page, name="article"),
    path("load-more/", load_more, name="load_more"),
    path("load-more-2/", load_more_2, name="load_more_2"),

]
