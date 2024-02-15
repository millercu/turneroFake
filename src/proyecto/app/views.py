from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views import View


from .models import Identificarse

# Create your views here.

class LoguearUsuario(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('prueba')
    

class RegistrarUsuario(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    field = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('prueba')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(RegistrarUsuario, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('prueba')
        return super(RegistrarUsuario, self).get(*args, **kwargs)

class ListaPendiente(LoginRequiredMixin, ListView):
    model = Identificarse
    template_name = 'base/categorias.html'
    context_object_name = 'categoria'

    # Esto es para que cada usuario tenga su pantalla,datos
    '''def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria'] = context['categoria'].filter(usuario=self.request.user)

        # Boton de buscar
        valor_buscado = self.request.GET.get('buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado

        return context'''
        
class Citas(LoginRequiredMixin, DetailView):
    model = Identificarse
    context_object_name = 'citas'
    template_name = 'base/citas.html'
    
def turnero(request):
    # Obtener el número actual del turno de la sesión
    turno_actual = request.session.get('turno_actual', 1)
    
    if request.method == 'POST':
            # Incrementar el número del turno
        turno_actual += 1
        request.session['turno_actual'] = turno_actual
        return JsonResponse({'turno': turno_actual})

    return render(request, 'citas.html', {'turno_actual': turno_actual})
    


class TurneroView(LoginRequiredMixin, View):
    def get(self, request):
        # Obtener el número actual del turno de la sesión
        turno_actual = request.session.get('turno_actual', 1)
        return render(request, 'citas', {'turno_actual': turno_actual})
    
    def post(self, request):
        # Obtener el número actual del turno de la sesión
        turno_actual = request.session.get('turno_actual', 1)
        # Incrementar el número del turno
        turno_actual += 1
        request.session['turno_actual'] = turno_actual
        return JsonResponse({'turno': turno_actual})

def generar_turno(request):
    def generar():
        for i in range(1,100):
            yield i 
    turno = generar()
    return JsonResponse({'turno': next(turno)})
 