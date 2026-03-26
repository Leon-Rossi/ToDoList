from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import ToDo
from .models import List
from .models import DateModel

# Create your views here.
def addToDo(request):
    if(request.GET.get("text") != None):
        textIn=request.GET.get("text")
        priorityIn=int(request.GET.get("priority", 0))

        try: 
            listIn=List.objects.get(name=request.GET.get("list"))
        except: 
            listIn=List.objects.get(id=List.get_default_pk())

        ToDo(text=textIn, priority=priorityIn, list=listIn).save()
        return HttpResponse("Success! added to " + listIn.name)
    else:
        return HttpResponse("Missing input")

def deleteToDo(request):
    if(request.GET.get("id") != None):
        ToDo.objects.get(id=request.GET.get("id")).delete()
        return HttpResponse("Sucess!")
    else:
        return HttpResponse("Missing input")

def showList(request):
    outputList = List.objects.all().values()
    template = loader.get_template("list.html")
    context = {
            "List" : outputList,
            }

    return HttpResponse(template.render(context, request))

def addList(request):
    if(request.GET.get("name") != None):
        List(name=request.GET.get("name")).save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Missing input")

def deleteList(request):
    if(request.GET.get("name") != None):
        List.objects.get(name=request.GET.get("name")).delete()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Missing input")

def showSpecificList(request, listName="ToDo"):
    checkDaily()
    if(List.objects.filter(name=listName).exists()):
        outputList = ToDo.objects.filter(list__name=listName).order_by('priority').values()
        Title = listName
        template = loader.get_template("todo.html")
        context = {
            "List" : outputList,
            "Title" : Title,
            }

        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("list not found")

def checkDaily():
    reference = DateModel.get_default()

    if(reference.dateVar.date() != datetime.datetime.today().date()):
        updateDaily()

def updateDaily():
    if(List.objects.filter(name="Daily").count() == 0):

        List(name = "Daily").save()
    
    dailyList = ToDo.objects.filter(list__name="Daily")

    for x in dailyList:  
        ToDo(text=x.text, priority=x.priority, list=List.objects.get(id=List.get_default_pk())).save()  

    DateModel.get_default().save()
