from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BlogPost


def blog_list(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


def custom_blog(request):
    per_page = request.GET.get('per_page', 5)

    posts = BlogPost.objects.all()

    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/custom_blog.html', {
        'page_obj': page_obj,
        'per_page': per_page,
    })
