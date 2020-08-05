from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'animal_index'),
    path('animals',views.animals, name = 'animals'),
    path('types',views.types, name = 'types'),
    path('rooms',views.rooms, name = 'rooms'),
    path('animals/<int:key>',views.animal, name = 'animal'),

    path('types/<str:name>',views.type, name = 'type'),
    path('add/type',views.add_type, name = 'add_type'),


    ]
