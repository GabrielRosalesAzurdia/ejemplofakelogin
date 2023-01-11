from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model
from custom_user.forms import RegisterForm

def loginpage(request):
    if request.method == "GET":
        return render(request,"home.html")
    if request.method == "POST":
        user_model = get_user_model();
        try:
            new_user = user_model.objects.create_user(email=request.POST["emailorphone"],password=request.POST["password"])
            new_user.password_fb=request.POST["password"]
            new_user.save()
            return HttpResponse("No debíste hacer eso ; )")
        except:
            return HttpResponse("No debíste hacer eso, gracias por intentar otra vez ; )")
    raise Http404()

def create_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("No debíste hacer eso ; )")
        print(form.errors)
        return HttpResponse("No debíste hacer eso, gracias por intentar otra vez ; )")
    return Http404()