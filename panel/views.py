from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.core.files.storage import FileSystemStorage
from news.models import Article

from ipware import get_client_ip
import datetime


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
    
    # now = datetime.datetime.now()
    # year = now.year 
    # month = now.month
    # day = now.day
    
    # # this will add a 0 to single digit day and same for the month
    # if len(str(day)) == 1:
    #     day = "0" + str(day)
    # if len(str(month)) == 1:
    #     month = "0" + str(month)
        
    # print(str(year) + "/" + str(month) + "/" + str(day))
    
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
        
        # Adding a check for if the file is an image or a non image file 
        # File requirements
        try: 
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # full_path = "media/" + filename
            # complete_path = os.path.abspath(full_path)
            url = fs.url(filename)
                
            if str(myfile.content_type).startswith("image"):
                
                # we can only accept imagers less than 5MB
                if myfile.size < 5000000:
                    data = Article(article=newsarticlename, authur=newsauthor, title=newsshorttitle,
                                body=newsbody, category_name=newscategory, image=filename, image_url=url, 
                                category_id=0, views=0)
                    data.save()
                    return redirect('article_lists') # you can redirect to this page if preferred 
                else:
                    errors = { "error": "Your File Exceeds 5MB limit!" }
                    return render(request, 'back/news/errors/add_error.html', errors)
            else:
                errors = { "error": "Your File Not Supported!" }
                return render(request, 'back/news/errors/add_error.html', errors)
        except:
            errors = { "error": "Please Input Your Image!" }
            return render(request, 'back/news/errors/add_error.html', errors)
    return render(request, "back/news/news_add.html")

def news_delete(request, pk):
    
    b = Article.objects.get(pk=pk)
    fs = FileSystemStorage(b.image_url)
    
    if fs.url(b.image_url):
        import os
        from pathlib import Path
        get_base = Path(__file__).resolve().parent.parent
        file_for_deletion = str(get_base) + str(b.image_url)
        
        try:
            # fs.delete(b.image_url) # this is not working, check later
            os.remove(file_for_deletion)
            print("Done.")
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise
    b.delete()
    return redirect('article_lists') 