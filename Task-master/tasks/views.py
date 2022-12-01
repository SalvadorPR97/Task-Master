from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone

from . import models
from . import forms

def homepage(request):
    hoy = timezone.now().date()
    tareas = (models.Task.objects
              .filter(finished=False)
              .select_related('project')
    )
    return render(request, 'tasks/homepage.html', {
        'fecha' : hoy,
        'tareas' : tareas,
    })

def lista_proyectos(request):
    projects = models.Project.objects.all()
    return render(request, 'tasks/projects.html', {
        'projects' : projects,
    })
    
def tareas_urgentes(request):
    tareas = (models.Task.objects
        .filter(priority='H')
        .exclude(finished=True)
        .order_by('name', 'orden')
    )
    return render(request, 'tasks/tareas_urgentes.html', {
        'tareas' : tareas,
    })
    
def tareas_no_urgentes(request):
    tareas = (models.Task.objects
        .all()
        .filter(priority='L')
        .filter(finished=False)
        .order_by('orden', '-name')
    )
    return render(request, 'tasks/tareas_no_urgentes.html', {
        'tareas' : tareas,
    })

def detalle_proyecto(request, pk):
    project = models.Project.objects.get(pk=pk)
    tareas = project.task_set.all()
    return render(request, 'tasks/detalle_proyecto.html', {
        'project' : project,
        'tareas' : tareas,
    })
def detalle_proyecto_code(request, code):
    project = models.Project.objects.get(code=code)
    tareas = project.task_set.all()
    return render(request, 'tasks/detalle_proyecto.html', {
        'project' : project,
        'tareas' : tareas,
    })
    
def buscar_tareas(request):
    tareas = []
    num_tareas = 0
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            priority = form.cleaned_data['priority']
            tareas = models.Task.objects.filter(name__icontains=query)
            
            if priority:
                tareas = tareas.filter(priority__in=priority)
                
            num_tareas = tareas.count()
    else:
        form = forms.SearchForm()
    return render(request, 'tasks/buscar_tareas.html', {
        'form' : form,
        'tareas' : tareas,
        'num_tareas' : num_tareas,
    })
    
def crear_proyecto(request):
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/projects/')
    else:
        form = forms.ProjectForm()
    return render(request, 'tasks/crear_proyecto.html', {
        'form' : form
    })

def crear_tareas(request):
    if request.method =='POST':
        form = forms.TasksForm(request.POST)
        if form.is_valid():
            tasks = form.cleaned_data['tasks']
            for task in tasks.split("\n"):
                new_task = models.Task(name=task)
                new_task.save()
            return redirect('/')
    else:
        form = forms.TasksForm()
    return render(request, 'tasks/crear_tareas.html', {
        'form' : form
    })
