from django.http.response import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import currencySerializer, selectionSerializer,compoundsSerializer

from json import dumps

from .models import currency, itemlist,vendor,selection,compounds
from request import serializers

# Create your views here.
class selectionlist(APIView):
    def get(self,request):
        selection1=selection.objects.all()
        serializer=selectionSerializer(selection1,many=True)
        return Response(serializer.data)


class compoundslist(APIView):
    def get(self,request):
        compounds1=compounds.objects.all()
        serializer = compoundsSerializer(compounds1,many=True)
        return Response(serializer.data)

class currencylist(APIView):
    def get(self,request):
        currency1=currency.objects.all()
        serializer = currencySerializer(currency1,many=True)
        return Response(serializer.data)


        
def index(request):
    if request.method == "GET":
        return render(request,"request/index.html",{
            "vendorlist":vendor.objects.all(),
            "list9":selection.objects.all(),
            "itemlist" : itemlist.objects.all()
        })
    elif request.method == "POST":
        check = selection.objects.all()
        if(request.POST["firstcatagory"] == "Consumable"):
            firstcatagory = request.POST["firstcatagory"]
            secondcatagoryid = request.POST["secondcatagory"]
            bhoo = int(secondcatagoryid)
            #this is to alot a secondcatagory as i get the result in id so i made a for loop and assign subcatagory whose id mathes
            for foo in check:
                if(foo.id == bhoo):
                    secondcatagory = foo.subcatagory1
            if(secondcatagoryid=="1" or secondcatagoryid=="2"):
                if(request.POST["thirdcatagoryselect"]=="17"):
                    fourthcatagory = request.POST["fourthcatagoryinput"]
                    name = f"{fourthcatagory}({firstcatagory}/{secondcatagory}/other)"
                else:
                    bhoo = int(request.POST["thirdcatagoryselect"])
                    for foo in check:
                        if(foo.id == bhoo):
                            thirdcatagoryselect = foo.subcatagory1
                    name = f"{thirdcatagoryselect}({firstcatagory}/{secondcatagory})"
                    
            elif(secondcatagoryid=="3" or secondcatagoryid=="4"):
                thirdcatagoryinput = request.POST["thirdcatagoryinput"]
                name = f"{thirdcatagoryinput}({firstcatagory}/{secondcatagory})"
            elif(secondcatagoryid=="5"):
                if(request.POST["thirdcatagoryselect"]=="28"):
                    fourthcatagory = request.POST["fourthcatagoryinput"]
                    name = f"{fourthcatagory}({firstcatagory}/{secondcatagory}/other)"
                else:
                    bhoo = int(request.POST["thirdcatagoryselect"])
                    for foo in check:
                        if(foo.id == bhoo):
                            thirdcatagoryselect = foo.subcatagory1
                    name = f"{thirdcatagoryselect}({firstcatagory}/{secondcatagory})"


            elif(secondcatagoryid=="6"):
                if(request.POST["thirdcatagoryselect"]=="34"):
                    fourthcatagory = request.POST["fourthcatagoryinput"]
                    name = f"{fourthcatagory}({firstcatagory}/{secondcatagory}/other)"
                else:
                    bhoo = int(request.POST["thirdcatagoryselect"])
                    for foo in check:
                        if(foo.id == bhoo):
                            thirdcatagoryselect = foo.subcatagory1
                    name = f"{thirdcatagoryselect}({firstcatagory}/{secondcatagory})"
            elif(secondcatagoryid=="7"):
                thirdcatagoryinput = request.POST["thirdcatagoryinput"]
                name = f"{thirdcatagoryinput}({firstcatagory}/{secondcatagory})"


            quantityinput = request.POST["quantityinput"]
            quantityunit = request.POST["quantityunit"]
            expectedcostinput = request.POST["expectedcostinput"]
            expectedcostcurrency = request.POST["expectedcostcurrency"]
            vendorinput = request.POST["vendorinput"]
            quantity = f"{quantityinput} {quantityunit}"
            ammount = f"{expectedcostinput} {expectedcostcurrency}"
            vendor1 = f"{vendorinput}"

            
            p=itemlist(name=name,quantity = quantity,ammount = ammount,vendor = vendor1)
            p.save()
            return HttpResponseRedirect(reverse("request:index"))
            



def p2(request):
    if request.method == "GET":
        return render(request,"request/vendoradd.html")
    elif request.method == "POST":
         name=request.POST["vendorname"]
         location=request.POST["vendorlocation"]
         code = request.POST["vendorcode"]
         bank =request.POST["vendorbank"]
         accno=request.POST["vendoraccountno"]
         route=request.POST["vendorroutinginformation"]
         currency=request.POST["vendorprefferedcurrency"]
         p=vendor(name=name,location=location,code=code,bank=bank,accno=accno,route=route,currency=currency)
         p.save()

         return render(request,"request/popup.html",{
            "p":p
        })