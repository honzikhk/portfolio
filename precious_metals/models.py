from django.db import models

class Metal(models.Model):
    GOLD = "Au"
    SILVER = "Ag"
    PLATINUM = "Pt"

    TYPE_OF_METAL_CHOICES = [
        (GOLD, "Gold"),
        (SILVER, "Silver"),
        (PLATINUM, "Platinum"),
    ]

    type_of_metal = models.CharField(choices=TYPE_OF_METAL_CHOICES, max_length=10)
    value_USD = models.IntegerField()

    # note = models.CharField(null=True, blank=True, max_length=255)
    # stored = models.CharField(max_length=40)
    # created = models.DateTimeField(auto_now_add=True)

    # add kind?(coins, bricks) A lot of choises... maybe impossible

    def __str__(self):
        return self.type_of_metal       # represent objects by their names in admin page

