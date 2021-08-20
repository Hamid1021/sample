from django.shortcuts import render
from django.core.paginator import Paginator
from home_gallery.models import Gallery_Home
from seo.models import Seo


def Home(request):
    seo_information = Seo.objects.all().filter(status=True).last()
    imags = Gallery_Home.objects.all().filter(status=True)
    page = Paginator(imags, 7)
    context = {
        "seo": seo_information,
        "object_list": page
    }
    return render(request, "home.html", context)
