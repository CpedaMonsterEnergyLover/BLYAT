from django.db import models


class Cruise(models.Model):
    name = models.CharField(max_length=60)
    days = models.IntegerField(verbose_name="длительность")
    length = models.IntegerField(verbose_name="протяженность")
    stops = models.IntegerField(verbose_name="кол-во остановок")


class Liner(models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField(verbose_name="регистрационный номер")
    team = models.IntegerField(verbose_name="кол-во членов команды")
    tickets = models.IntegerField(verbose_name="стоимость билетов")


class Excursion(models.Model):
    date = models.DateField(verbose_name="дата_отбытия")
    tickets = models.IntegerField(verbose_name="продано билетов")
    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)
    liner = models.ForeignKey(Liner, on_delete=models.CASCADE)
