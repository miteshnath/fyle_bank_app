from django.db import models


class Bank(models.Model):
    ifsc = models.CharField(max_length=20)
    bank_id = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.bank_name
