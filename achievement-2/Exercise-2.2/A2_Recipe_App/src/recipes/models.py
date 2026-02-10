from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length = 120)
    description = models.TextField()
    cooking_time = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

        
