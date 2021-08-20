from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from seo.models import Seo
from blog.models import Article, Comment

from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

from blog.forms import CommentForm
# Create your views here.


def blog_page(request):
    global results_per_page
    results_per_page = 3  # change it if you want
    articles = Article.objects.all().filter(status="p")[:results_per_page]
    seo_information = Seo.objects.all().filter(status=True).last()
    count_articles = Article.objects.all().filter(status="p").count
    context = {
        "seo": seo_information,
        "articles": articles,
        "count_articles": count_articles,
        "results_per_page": results_per_page,
    }

    return render(request, "blog.html", context)


def load_more(request):
    page = request.POST.get('page')
    articles = Article.objects.published()
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


def article_page(request, pk, slug):
    global results_per_page_comments
    results_per_page_comments = 5  # change it if you want
    seo_information = Seo.objects.all().filter(status=True).last()
    object = get_object_or_404(Article, pk=pk, slug=slug)
    form = CommentForm(request.POST or None)
    comments = Comment.objects.get_object_or_None(
        article=object)[:results_per_page_comments]
    count_comments = Comment.objects.get_count(article=object)
    context = {
        "object": object,
        "seo": seo_information,
        "form": form,
        "comments": comments,
        "count_comments": count_comments,
        "results_per_page_comments": results_per_page_comments,
        "pk": pk,
        "slug": slug,
    }
    if form.is_valid():
        full_name = form.cleaned_data.get("full_name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        try:
            Comment.objects.create(fullname=full_name, email=email,
                                   message=message, article=object)
            context["message"] = "نظر شما ارسال گردید و منتظر تایید مدیر می باشد"
        except:
            context["message_1"] = "نظر شما ارسال نگردید دوباره تلاش نمایید"
        finally:
            context["form"] = CommentForm()

    return render(request, "article.html", context)


def load_more_2(request):
    page = request.POST.get('page')
    pk = request.POST.get('pk')
    slug = request.POST.get('slug')
    object = get_object_or_404(Article, pk=pk, slug=slug)
    comments = Comment.objects.get_object_or_None(article=object)
    paginator = Paginator(comments, results_per_page_comments)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    posts_html = loader.render_to_string(
        'Base/comments.html',
        {'comments': posts}
    )

    output_data = {
        'posts_html': posts_html,
        'has_next': posts.has_next(),
    }

    return JsonResponse(output_data)
