from django.shortcuts import render

from .models import Article


def articles_list(request):
    ordering = '-published_at'
    context = {'object_list': Article.objects.all().order_by(ordering)}
    return render(request=request, template_name='news/news.html', context=context)
