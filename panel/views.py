from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from news.models import Article

from ipware import get_client_ip

def panel(request):
    
    ip, ip_routable = get_client_ip(request)
    
    if ip is None:
        ip = "0.0.0.0"
    else:
        if ip_routable:
            ipv = "Public"
        else:
            ipv = "Private"
    print(ip, ipv)
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'back/home.html', context)
    
class ArticleListView(ListView):
    
    model = Article
    news = Article.objects.all()
    context_object_name = 'articles'    
    template_name = "back/news/news_lists.html"

def news_add(request):
    
    if request.method == "POST":
        newsarticlename = request.POST.get('newsarticlename')
        newsauthor = request.POST.get('newsauthor')
        newscategory = request.POST.get('newscategory')
        newsshorttitle = request.POST.get('newsshorttitle')
        newsbody = request.POST.get('newsbody')
        
        # User requirements for creating and article
        if newsauthor == "" or newsshorttitle == "" or newsbody == "" or newscategory == "":
            errors = {
                "error": "All Fields Required!",
            }
            return render(request, 'back/news/errors/add_error.html', errors)
        
        # File requirements
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        data = Article(article=newsarticlename, authur=newsauthor, title=newsshorttitle,
                       body=newsbody, category_name=newscategory, image=filename, image_url=url, category_id=0, views=0)
        data.save()
        # return redirect('newsList') you can redirect to this page if preferred 
    return render(request, "back/news/news_add.html")