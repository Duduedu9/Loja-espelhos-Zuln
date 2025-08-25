
from django.urls import path
from .views import ListaEspelhosView, DetalheEspelhoView

app_name = 'loja'
urlpatterns = [
   
    path('', ListaEspelhosView.as_view(), name='lista'),


    path('espelho/<int:pk>/', DetalheEspelhoView.as_view(), name='detalhe'),
]