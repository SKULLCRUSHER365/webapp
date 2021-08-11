from django.db import models

# Create your models here.
class selection(models.Model):
    catagory = models.CharField(max_length=64)
    subcatagory1 = models.CharField(max_length=64)

class compounds(models.Model):
    chemicalformulla = models.CharField(max_length=64)
    compoundname = models.CharField(max_length=64)
    casrn = models.CharField(max_length=64)

class currency(models.Model):
    symbol = models.CharField(max_length=3)

class vendor(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    bank = models.CharField(max_length=64)
    accno = models.CharField(max_length=64)
    route = models.CharField(max_length=64)
    currency = models.CharField(max_length=64)

class itemlist(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=64)
    ammount = models.CharField(max_length=64)
    vendor = models.CharField(max_length=64)