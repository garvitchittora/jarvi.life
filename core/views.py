from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .serializers import *
import json

def home_page(request):
   url = request.META['HTTP_HOST']
   results = {}
   if Site.objects.filter(site_url=url).exists():
      site = Site.objects.get(site_url=url)
      site_data = SiteSerializer(site).data
      results.update(site_data)
      
      if Company.objects.filter(site=site).exists():
         data = Company.objects.filter(site=site)
         data_serializer = CompanySerializer(data, many=True).data
         results.update({"company": json.loads(json.dumps(data_serializer))})
      
      if FewPoint.objects.filter(site=site).exists():
         data = FewPoint.objects.filter(site=site)
         data_serializer = FewPointSerializer(data, many=True).data
         results.update({"few_points": json.loads(json.dumps(data_serializer))})

      if CoverImage.objects.filter(site=site).exists():
         data = CoverImage.objects.filter(site=site)
         data_serializer = CoverImageSerializer(data, many=True).data
         results.update({"cover_image": json.loads(json.dumps(data_serializer))})

      if Pics.objects.filter(site=site).exists():
         pics = Pics.objects.get(site=site)
         pictures = pics.content
         results.update({"pictures": pictures})

   return render(request, "home_page.html", results)

def todo_page(request):
   if request.user.is_authenticated:
      url = request.META['HTTP_HOST']
      results = {}
      if Site.objects.filter(site_url=url).exists():
         site = Site.objects.get(site_url=url)
         site_data = SiteSerializer(site).data
         results.update(site_data)
         
         if FewPoint.objects.filter(site=site).exists():
            data = FewPoint.objects.filter(site=site)
            data_serializer = FewPointSerializer(data, many=True).data
            results.update({"few_points": json.loads(json.dumps(data_serializer))})

         if Todo.objects.filter(site=site).exists():
            data = Todo.objects.filter(site=site)
            data_serializer = TodoSerializer(data, many=True).data
            results.update({"todo": json.loads(json.dumps(data_serializer))})
         
         if BucketList.objects.filter(site=site).exists():
            pics = BucketList.objects.get(site=site)
            pictures = pics.content
            results.update({"pictures": pictures})

      return render(request, "todo.html", results)
   else:
      return redirect("/")

def login_page(request):
   if request.user.is_authenticated:
      return redirect('/') 
   else:
      url = request.META['HTTP_HOST']
      results = {}
      if Site.objects.filter(site_url=url).exists():
         site = Site.objects.get(site_url=url)
         site_data = SiteSerializer(site).data
         results.update(site_data)
         if FewPoint.objects.filter(site=site).exists():
            data = FewPoint.objects.filter(site=site)
            data_serializer = FewPointSerializer(data, many=True).data
            results.update({"few_points": json.loads(json.dumps(data_serializer))})

      if request.method == 'POST':
         password=request.POST['password']
         username=request.POST['username']
         user = authenticate(username=username, password=password)
         if user:
               login(request, user)
               return redirect("/")
         else:
               messages.add_message(request, messages.SUCCESS, 'Incorrect Email Or Password')
                   
   return render(request, 'login.html', results)