from django.db import models


class CryptoCurrency(models.Model):

    name = models.CharField(max_length=30)
    amount = models.FloatField()
    saved_on = models.CharField(max_length=30, default="very safe place")
    note = models.CharField(null=True, blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        # represent objects by their names in admin page