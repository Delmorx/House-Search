from django.db import models

# Create your models here.

class Listing(models.Model):
    link = models.URLField()
    address = models.CharField(max_length=255)
    distance_to_work = models.FloatField(help_text="Distance to work in miles")
    distance_to_school = models.FloatField(help_text="Distance to school in miles")
    distance_to_other = models.FloatField(help_text="Distance to other location in miles")
    bedrooms = models.IntegerField()
    square_footage = models.IntegerField()
    bathrooms = models.FloatField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.address} ({self.bedrooms}bd/{self.bathrooms}ba)"
