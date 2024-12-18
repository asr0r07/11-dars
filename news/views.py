from django.shortcuts import render
from.models import News


def home(request):
    articles = News.objects.all()
    ctx = {'articles': articles}
    return render(request, 'index.html', ctx)


def news_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        category = request.POST.get('category')
