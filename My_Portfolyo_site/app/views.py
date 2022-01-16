from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Contact, Article

def index(request):
          if request.method=="POST":
                    contact=Contact()
                    name=request.POST.get('name')
                    email=request.POST.get('email')
                    subject=request.POST.get('subject')
                    contact.name=name
                    contact.email=email
                    contact.subject=subject
                    contact.save()
                    return HttpResponse("<h1> THANKS FOR CONTACT US</h1>")

          return render(request, 'index.html')



class Blog_View(ListView):
    model = Article
    template_name = 'blog.html'
''
class Blog_Detail_View(DetailView):
    model = Article
    template_name = 'blog-single.html'
