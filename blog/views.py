from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog.models import Topblog,Comments
from django.contrib import messages
from blog.templatetags import extras
# Create your views here.
import json


def index(request):
    data = Topblog.objects.all()
    blogs = {
        'blogs': data
    }
    return render(request, 'blog/index.html', blogs)


def blogview(request, id):

    blog = Topblog.objects.filter(id=id).first()
    comment = Comments.objects.filter(post=blog,parent=None)
    replies = Comments.objects.filter(post=blog).exclude(parent=None)
    if blog.views>=1:
        views = blog.views
        
    else:
        views = ''
    if comment.count()>=1:
        comm = comment.count()
        
    else:
        comm = ''

    repDict = {}
    for reply in replies:
        if reply.parent.id not in repDict.keys():
            repDict[reply.parent.id] = [reply]
        else:
            repDict[reply.parent.id].append(reply)
    print(repDict)
    blogs = {'blogs': blog,
     'id': id,
     'views':views,
     'comments':comment,
     'user':request.user,
     'comm':comm,
    'repDict':repDict
     }
    blog.views = blog.views+1
    blog.save()
    return render(request, 'blog/readtheblog.html', blogs)


def newblog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        data = request.POST.get('htmlcode')
        blogid = request.POST.get('blogid')
        desc = request.POST.get('desc')
        print(title, data, blogid, desc)
        if blogid != "":
            Topblog.objects.filter(id=blogid).update(
                title=title, content=data, desc=desc)

        else:
            content = Topblog(content=data, title=title, desc=desc)
            content.save()

        messages.success(request, 'Contact request submitted successfully.')
        return HttpResponse('Hello')

    else:
        allblogs = Topblog.objects.all()
        blogjson = {}
        for item in allblogs:
            blogjson[item.id] = [item.title, item.content, item.id, item.desc
                                 ]
        blogs = {'blogs': allblogs, 'blogjson': json.dumps(blogjson)}
        return render(request, 'blog/create_new.html', blogs)

def delete(request):
    if request.method == "POST":
        blogid = request.POST.get('blogid')
        print(blogid)
        Topblog.objects.filter(id=blogid[1:]).delete()

    return HttpResponse(f'The Item is :{request}')

def Postcomment(request):
    if request.method=="POST":
        comment = request.POST.get('comment')
        user = request.user
        postid = request.POST.get('postid')
        commid = request.POST.get('commid')

        print(commid)
        post = Topblog.objects.get(id=postid)

        if commid=="":
            comment = Comments(comment = comment,user=user,post = post)
            comment.save()
            messages.success(request, 'Your Comment successfully sended.')
        else:
            parent = Comments.objects.get(id = commid)
            print(parent)
            comment = Comments(comment = comment,user=user,post = post,parent=parent)
            comment.save()
            messages.success(request, 'Your Reply successfully sended.')



    return redirect(f'/showblogs/readblog_ID={postid}')