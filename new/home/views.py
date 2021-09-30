# I am create this file
from home.models import Item
from django.shortcuts import render
from home.models import Item
from datetime import datetime


# Create your views here.
def survey(request):
    dataDisplay=Item.objects.all()
    return render (request, 'Survey.html', {"data":dataDisplay})
   

def index(request):
   if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        address2=request.POST.get('address2')
        City_Village=request.POST.get('City_Village')
        atta=request.POST.get('atta')
        dic=request.POST.get('dic')
        zip=request.POST.get('zip')
        index=Item(name=name, email=email, phone=phone, address=address, address2=address2, dic=dic, zip=zip, atta=atta, City_Village=City_Village, date= datetime.today())
        index.save()
   return render(request, 'index.html')

 
