from django.urls import path
from .views import LoguearUsuario, ListaPendiente, RegistrarUsuario, Citas, generar_turno, turnero
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ListaPendiente.as_view(), name = 'prueba'),
               path('login/', LoguearUsuario.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('registro/', RegistrarUsuario.as_view(), name='registro'),
               path('citas/<int:pk>', Citas.as_view(), name='citas'),
               path('turnero/', turnero, name='turnero')]