from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    calorie = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + str(self.calorie) + ' calories'
