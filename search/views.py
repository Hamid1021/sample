from django.shortcuts import render
from blog.models import Article
from seo.models import Seo
from django.db.models import Q


from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# Create your views here.


def search(request):
    sear = request.GET.get("q")
    if sear == None:
        sear = "e"
    print(sear)
    global results_per_page
    results_per_page = 3  # change it if you want
    query = Q(title__icontains=sear) | Q(
        keyword__keyword__icontains=sear) | Q(description__icontains=sear) | Q(
            category__title__icontains=sear)

    articles = Article.objects.all().filter(
        query, status="p").distinct()[:results_per_page]

    seo_information = Seo.objects.all().filter(status=True).last()
    count_articles = Article.objects.all().filter(query, status="p").distinct().count
    context = {
        "seo": seo_information,
        "articles": articles,
        "count_articles": count_articles,
        "results_per_page": results_per_page,
        "sear": sear,
    }

    return render(request, "search.html", context)


def load_more(request):
    page = request.POST.get('page')
    sear = request.POST.get('sear')
    query = Q(title__icontains=sear) | Q(
        keyword__keyword__icontains=sear) | Q(description__icontains=sear) | Q(
            category__title__icontains=sear)
    articles = articles = Article.objects.all().filter(
        query, status="p").distinct()
    paginator = Paginator(articles, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    posts_html = loader.render_to_string(
        'Base/articles.html',
        {'articles': posts}
    )

    output_data = {
        'posts_html': posts_html,
        'has_next': posts.has_next(),
    }

    return JsonResponse(output_data)
