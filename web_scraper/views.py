from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, 'web_scraper/post_list.html', {})


def offer_list(request):
    return render(request, 'web_scraper/offer_list.html', {})