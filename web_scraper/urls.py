from django.urls import path
from django.views.static import serve

from config import settings
from . import views

urlpatterns = [
    path('', views.offer_list, name='offer_list'),  # this is the home page
]

if not settings.DEBUG:
    urlpatterns += [
        path('static/', serve, {'document_root': settings.STATIC_ROOT}),
    ]
