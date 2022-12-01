"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import tasks.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('buscar/', tasks.views.buscar_tareas, name='buscar'),
    path('', tasks.views.homepage),
    path('high/', tasks.views.tareas_urgentes, name='tareas_urgentes'),
    path('low/', tasks.views.tareas_no_urgentes, name='tareas_no_urgentes'),
    path('projects/', tasks.views.lista_proyectos, name='proyectos'),
    path('projects/<int:pk>/', tasks.views.detalle_proyecto, name='detalle_proyecto'),
    path('projects/new/', tasks.views.crear_proyecto, name='crear_proyecto'),
    path(
        'projects/<slug:code>/', 
        tasks.views.detalle_proyecto_code, 
        name='proyecto_por_codigo'),
    path('newtasks/', tasks.views.crear_tareas, name='crear_tareas'),
    
]
