from django.shortcuts import render
from .models import Pics

def home_page(request):
   pics = Pics.objects.first()
   content = pics.content
   return render(request, "home_page.html", {"content": content})