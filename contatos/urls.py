from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:contato_id>',views.ver_contato,name='ver_contato'), # aqui e um novo endpoint 
]          # aqui ele ta buscando o id do contato
