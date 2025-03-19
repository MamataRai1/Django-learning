from django.shortcuts import render,redirect
from django.http import request
from  .models import person

def home(request):
    if request.method=='POST':
        name=request.POST["name"]
        p=person.objects.create(name=name)
        p.save()
        return redirect('home')
    return render(request,"index.html")
