from django.urls import path
from . import views

urlpatterns = [
        path("add/", views.addToDo, name="addToDo"),
        path("delete/", views.deleteToDo, name="deleteToDo"),
        path("addList/", views.addList, name="addList"),
        path("deleteList/", views.deleteList, name="deleteList"),
        path("list/", views.showList, name="showList"),
        path("", views.showSpecificList, name="showSpecificList"),
        path("<str:listName>/", views.showSpecificList, name="showSpecificList"),
]
