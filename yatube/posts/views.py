from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.template import loader


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'templates/posts/index.html', context)




def group_list(request):
    template = 'templates/posts/group_list.html'
    return render(request, template)


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    template = 'templates/posts/group_posts.html'
    title = "Здесь будет информация о группах проекта Yatube"
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
#    return HttpResponse(f'Группа с названием {slug}')


#def group_posts(request, slug):
#    return HttpResponse(f'Группа с названием {slug}')
