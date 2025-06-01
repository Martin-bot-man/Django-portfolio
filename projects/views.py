from django.shortcuts import render
from projects.models import Project

def Project_index(request):
    projects = Project.objects.all()
    context ={
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

# Create your views here.
