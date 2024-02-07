from django.urls import path
from galeria.views import index, imagem

#  end points
urlpatterns = [
    path('', index, name="index"),
    path('imagem/', imagem, name="imagem")
]



