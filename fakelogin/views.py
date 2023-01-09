from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model

def loginpage(request):
    if request.method == "GET":
        return render(request,"home.html")
    if request.method == "POST":
        user_model = get_user_model();
        try:
            new_user = user_model.objects.create_user(email=request.POST["emailorphone"],password=request.POST["password"])
            new_user.save()
            return HttpResponse("No debíste hacer eso ; )")
        except:
            return HttpResponse("No debíste hacer eso, gracias por intentar otra vez ; )")
    raise Http404()