from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from gallery.models import Gallery, Category
from seo.models import Seo

from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def gallery(request):
    global results_per_page
    results_per_page = 11  # change it if you want
    seo_information = Seo.objects.all().filter(status=True).last()
    imags = Gallery.objects.all().filter(status=True)[:results_per_page]
    Categories = Category.objects.all().filter(status=True)
    count_gallery = Gallery.objects.all().filter(status=True).count
    context = {
        "seo": seo_information,
        "object_list": imags,
        "categories": Categories,
        "count_gallery": count_gallery,
        "results_per_page": results_per_page,
    }

    return render(request, "gallery.html", context)


def load_more(request):
    page = request.POST.get('page')
    imags = Gallery.objects.all().filter(status=True)
    paginator = Paginator(imags, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    posts_html = loader.render_to_string(
        'Base/images.html',
        {'object_list': posts}
    )

    output_data = {
        'posts_html': posts_html,
        'has_next': posts.has_next(),
    }

    return JsonResponse(output_data)
