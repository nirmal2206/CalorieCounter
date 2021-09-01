from django.db import models

class NutritionFactsLabel(models.Model):
    food_name = models.CharField(max_length=50, default='')
    serving_size = models.IntegerField(default=100, help_text='Serving size in grams.')
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.food_name.title()

class ConsumedCalorie(models.Model):
    user = models.CharField(max_length=50)
    total_calorie = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.user
    