from django.conf.urls import url
from . import views
from scraper import settings

urlpatterns = [url(r'^$', views.offer_list, name='offer_list'),  # this is the home page
               url(r'^post/(\d+)/$', views.post_list, name='post_list'),
               ]
if not settings.DEBUG:
    urlpatterns += (
        (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
