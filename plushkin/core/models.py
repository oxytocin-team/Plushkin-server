from django.db import models


class Medicine(models.Model):
    title = models.CharField(max_length=256)


class Substances(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    doza = models.CharField(max_length=256)
