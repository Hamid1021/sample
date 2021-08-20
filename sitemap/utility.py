from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse

from blog.models import Article


class ArticleSitemap(Sitemap):
    changefreq = 'always'
    priority = 1

    def items(self):
        return Article.objects.filter(status="p")

    def lastmod(self, obj):
        return obj.publish


class StaticViewSitemap(sitemaps.Sitemap):
    changefreq = 'always'
    priority = 1

    def items(self):
        return ['gallery_home:home', 'gallery:gallery', "cantact:cantact", ]

    def location(self, item):
        return reverse(item)


##############################################################
SiteMaps = {}


def add_to_sitemaps(key, value, flag=0):
    # add
    if flag == 0:
        SiteMaps[key] = value
    # update
    else:
        SiteMaps.update({key: value})



add_to_sitemaps('static', StaticViewSitemap)
add_to_sitemaps('Article', ArticleSitemap)

