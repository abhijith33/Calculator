from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
# Create your views here.
# something

def cal(request):
    if request.method=='POST':
        a =calform(request.POST)
        if a.is_valid():
            fst=a.cleaned_data['first']
            scd=a.cleaned_data['second']
            opt=a.cleaned_data['option']
            if opt=='add':
                result=fst+scd
            elif opt=='sub':
                result=fst-scd
            elif opt=='mul':
                result=fst*scd
            elif opt=='div':
                result=fst/scd
            context = {'result': result}
            return render(request, 'calculator.html',context)
    return render(request, 'calculator.html')


def register(request):
    if request.method=='POST':
        a = regform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            pw = a.cleaned_data['password']
            cpw = a.cleaned_data['cpassword']
            if pw == cpw:
                b = regmodel(name=nm,email=em,phone=ph,password=pw)
                b.save()
                return HttpResponse("Successful")
            else:
                return HttpResponse("Incorrect password")
        else:
            return HttpResponse("Registration Failed")
    else:
        return render(request,'registration.html')



def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            pw = a.cleaned_data['password']
            b= regmodel.object.all()
            for i in b:
                if i.email==em and i.password==pw:
                    return HttpResponse("Login success")
            else:
                return HttpResponse("Login failed")
    else:
        return render(request,'login.html')



