from django.shortcuts import render
from .models import Blog, Comment
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
import random
import jieba
# Create your views here.

def board(req):
    template = loader.get_template('board/show.html')
    showlist,idlist=[],[]
    for i in range(40):
        x = random.randint(2,2500)
        if x not in idlist:
            idlist.append(x)
    for i in range(20):
        showlist.append(Blog.objects.get(id=idlist[i]))
    pages = {
        'indexes':idlist,
        'news':showlist,
    }
    return HttpResponse(template.render(pages,req))

def show(req, id):
    blog = Blog.objects.get(id=id)
    template = loader.get_template('board/index.html')
    context = {
        'id': id,
        'time':blog.time,
        'title': blog.title,
        'content': blog.content.split('\n'),
        'comments': blog.comment_set.all(),
        'pic1':blog.pic1,
        'pic2':blog.pic2,
        'pic3':blog.pic3,
        'pic4':blog.pic4,
        'pic5':blog.pic5,
        'key1':blog.key1,
        'key2':blog.key2,
        'key3':blog.key3,

    }
    return HttpResponse(template.render(context, req))


def comment(req, id):
    data = req.POST
    user = data['user']
    content = data['content']
    blog = Blog.objects.get(id=id)
    obj = Comment(blog=blog, user=user, content=content)
    obj.full_clean()
    obj.save()
    return HttpResponseRedirect(f'/board/blog/{id}')

def list(req):
    template = loader.get_template('board/list.html')
    all_list = Blog.objects.all().order_by('-time')
    return HttpResponse(template.render({'all':all_list},req))

def search(req):
    data = req.GET.get('q')
    if not data:
        return HttpResponseRedirect('/board/list')
    keys = jieba.cut_for_search(data)
    bytitle = Blog.objects.filter(title__icontains=data)
    bytitle=bytitle.order_by('-time')
    bykeys = [Blog.objects.filter(key1__in=keys),Blog.objects.filter(key2__in=keys),Blog.objects.filter(key3__in=keys)]
    bykeys= [i.order_by('-time') for i in bykeys]
    bytext = Blog.objects.filter(content__icontains=data)
    bytext= bytext.order_by('-time')
    return render(req, 'board/search.html', {'bytitle':bytitle, 'bykeys':bykeys, 'bytext':bytext})