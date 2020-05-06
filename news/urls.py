from django.urls import path
from .views import index, details, create, edit, delete


urlpatterns = [
    path('', index),
    path('index', index),
    path('details', details),
    path('create', create),
    path('edit', edit),
    path('delete', delete)
]
