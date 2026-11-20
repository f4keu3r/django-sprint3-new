from django.shortcuts import render, get_object_or_404

from .models import Post, Category


# Выносим "магическое число" в именованную константу модуля
POSTS_PER_PAGE = 5


def index(request):
    post_list = Post.objects.available()[:POSTS_PER_PAGE]
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(
        Post.objects.available().with_relations(),
        pk=pk,
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.posts.published()
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
