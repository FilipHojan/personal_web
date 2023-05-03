from django.shortcuts import render, Http404, get_object_or_404
from .models import Post, Author, Category

import requests

# Create your views here.
def first_views(request):
    return render(request, 'myapp/first.html')


def home_views(request):
    return render(request, 'myapp/index.html')


def contact_views(request):
    return render(request, 'myapp/contact.html')


def about_views(request):
    return render(request, 'myapp/about.html')

def covid19_views(request, country_code=None, name=None):
    API_KEY = '2e31b03c3d514e98a70dc5a1af3b9f50'

    url = f'https://api.covid19api.com/summary'
    response = requests.get(url)
    data = response.json()
    # wyszukiwanie danych dla danego kraju
    for country in data['Countries']:
        if country['CountryCode'] == country_code:
            country_data = country
            break
    else:
        # jeśli nie znaleziono kraju o podanym kodzie, zwróć pusty słownik
        country_data = {}

    return render(request, 'myapp/covid19.html', {'context': data, 'country_code': country_code, 'country_data': country_data})

def blog_views(request, category_name=None):
    if category_name:
        queryset = Post.objects.filter(category__name=category_name, public=True)
    else:
        queryset = Post.objects.filter(public=True)

    context={
        'object_list': queryset.order_by('-date_publish'),
        'category_list': Category.objects.all(),
        'category_name': category_name,
    }
    return render(request, 'myapp/blog.html', context)

def blog_detail_views(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("404 - Page Not Found")
    context = {'object': post}
    return render(request, 'myapp/blog_detail.html', context)

def author_views(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author)

    context = {
        'author': author, 'posts': posts

    }
    return render(request, 'myapp/blog.html', context)