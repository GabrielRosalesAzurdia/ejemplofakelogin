from django.shortcuts import render
from django.http import HttpResponse, Http404

def loginpage(request):
    if request.method == "GET":
        return render(request,"home.html")
    if request.method == "POST":
        
        return HttpResponse("Hizo un post")
    raise Http404()