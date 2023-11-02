from django.shortcuts import render, HttpResponse


def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context={'title':'create a context for blog','context':'i created a context for blog single using jinja','author':'Younes Veisi'}
    return render(request, 'blog/blog-single.html',context)

