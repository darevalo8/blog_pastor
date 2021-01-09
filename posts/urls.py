from django.urls import path
from .views import inicio, bienvenida

app_name='posts'
urlpatterns = [
    path('', inicio, name="inicio"),
    path('bienvenida', bienvenida, name="bienvenida"),
]