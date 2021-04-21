from os import name
from django.forms import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if response.user.todolist.all():
        
        
        {"save":["save"], "c1":["clicked"]}
        if response.method == "POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()        
                
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                
                if len(txt) > 2:
                        ls.item_set.create(text=txt, complete=False)
                    
                else:
                        print("Invalid")  
        
        # return HttpResponse("<h2>%s</h2><p>%s</p>" % (ls.name, item.text))
        return render(response, "Myapp/list.html", {"ls":ls})
    return render(response, "Myapp/view.html", {})
    
def  home(response):
    return render(response, "Myapp/home.html", {})

def create(response):
    # response.user
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
            
        return HttpResponseRedirect("/%i" %t.id)    
    else:    
        form = CreateNewList()
    return render(response, "Myapp/create.html", {"form":form})     
    
def view(response):
        return render(response, "Myapp/view.html", {})