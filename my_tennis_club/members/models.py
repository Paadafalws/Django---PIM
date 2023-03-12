from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)



class compras(models.Model):

    Item = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
  
