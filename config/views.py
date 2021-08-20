from django.shortcuts import render

from seo.models import Seo


def HeaderRefrence(request):
    seo_information = Seo.objects.all().filter(status=True).last()
    context = {
        "seo": seo_information,
    }
    return render(request, 'Base/HeaderRefrence.html', context)


def Header(request):
    seo_information = Seo.objects.all().filter(status=True).last()
    context = {
        "seo": seo_information,
    }
    return render(request, "Base/Header.html", context)


def FooterRefrence(request):
    seo_information = Seo.objects.all().filter(status=True).last()
    context = {
        "seo": seo_information,
    }
    return render(request, "Base/FooterRefrence.html", context)


def Footer(request):
    seo_information = Seo.objects.all().filter(status=True).last()
    context = {
        "seo": seo_information,
    }
    return render(request, "Base/Footer.html", context)
