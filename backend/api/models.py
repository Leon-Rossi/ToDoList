from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=200)

    def get_default_pk():
        default, object = List.objects.get_or_create(name = "ToDo")
        return default.pk

class ToDo(models.Model):
    text = models.CharField(max_length=200)
    priority = models.IntegerField()
    list = models.ForeignKey(to=List, on_delete = models.CASCADE, default = List.get_default_pk)
    pub_date = models.DateTimeField(auto_now_add=True)

class DateModel(models.Model):
    dateVar = models.DateTimeField(auto_now = True)

    def get_default():
        default, object = DateModel.objects.get_or_create(id=0)
        return default
