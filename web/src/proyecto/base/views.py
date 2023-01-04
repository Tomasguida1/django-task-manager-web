from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea

class Logueo(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("Tareas")

class ListaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name =  "tareas"
    
    
class DetalleTarea(LoginRequiredMixin,DetailView):
    model = Tarea
    context_object_name = "tarea"
    template_name = "base/tarea.html"
    
class CrearTarea(LoginRequiredMixin,CreateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('Tareas') 
    
class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('Tareas') 

class EliminarTarea(LoginRequiredMixin,DeleteView):
        model = Tarea
        context_object_name = "tareas"
        success_url = reverse_lazy('Tareas') 

    