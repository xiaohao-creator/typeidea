"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.sitemaps import views as sitemaps_views

import xadmin
from autocomplete import CategoryAutocomplete, TagAutocomplete
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from blog.views import PostListView, PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView
from comment.views import CommentView
from config.views import LinkListView
from typeidea.custom_site import custom_site

urlpatterns = [
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemaps_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),

    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),


    # url(r'^super_admin/', admin.site.urls, name='super-admin'),
    # url(r'^admin/', custom_site.urls, name='admin'),
    url(r'^xadmin/', include(xadmin.site.urls), name='xadmin'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
