from itertools import count
import math
from django.shortcuts import render,HttpResponse, redirect
from .forms import ProjectForm,handle_uploaded_file
from django.core.files.storage import FileSystemStorage
import pandas as pd

# Create your views here.

def create_project(request):
    
    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect('/index.html')
    
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        
        if form.is_valid():
            print("El id de usuario es "+str(request.user.id))
            #
            project = form.save(commit=False)            
            project.usuario = request.user # add the current user as a related user
            project.save()
            project.set_columnas_originales(list(project.get_data().columns))
            project.save()
            return redirect('/projects/')
    else:
        form = ProjectForm()
    return render(request, 'crearProyectos.html', {'form': form})



def seeProyects(request):
    user = request.user
    print(user)
    if not user.is_authenticated:
        return redirect('/index.html')
    
    projects = request.user.projects.all()
    print(projects)
    return render(request,'menuProyectos.html',{'projects': projects})
    
    

