from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.offer_list, name='offer_list'),  # this is the home page
    url(r'^post/(\d+)/$', views.post_list, name='post_list'),
]