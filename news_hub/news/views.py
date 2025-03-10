from django.shortcuts import render
from django.views.generic import TemplateView


def news(request):
    return render(request, 'news/base.html')

# class NewsView(TemplateView):
#     template_name = 'base.html'
