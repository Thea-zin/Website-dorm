# models.py
import os

from django.db import models


def upload_path(instance, filename):
    return '/'.join(['covers', str(instance.title), filename])

class Book(models.Model):
    id = models.BigAutoField(primary_key=True) 
    title = models.CharField(max_length=32, blank=False)
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    description = models.TextField(blank=True)
    like_count = models.PositiveIntegerField(default=0)  # New field for like count

    
    def delete_description_file(self):
        # Get the path to the description file
        description_path = upload_path(self, self.title + '.txt')
        # Check if the description file exists and delete it
        if os.path.exists(description_path):
            os.remove(description_path)


