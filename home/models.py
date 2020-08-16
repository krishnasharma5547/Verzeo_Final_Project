from django.db import models

class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=10)
    
    def __str__(self):
        return self.name