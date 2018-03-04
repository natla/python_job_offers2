from django.shortcuts import render
from django.utils import timezone
from .models import Post
from . import scraping


# Create your views here.
def post_list(request, arg2):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'web_scraper/post_list.html', {'posts': posts})


def offer_list(request):
    job_list = scraping.print_jobs()
    return render(request, 'web_scraper/offer_list.html', {'offers': job_list})