from django.db import models

class AllData(models.Model):
    country_code=models.CharField(max_length=10)
    country_name=models.CharField(max_length=255)
    full_data = models.JSONField()
    
    def __str__(self):
        return self.country_name