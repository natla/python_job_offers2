from django.shortcuts import render

from . import scraping


def offer_list(request):
    job_list = scraping.print_jobs()
    return render(request, 'web_scraper/offer_list.html', {'offers': job_list})
