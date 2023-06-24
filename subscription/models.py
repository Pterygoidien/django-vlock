from django.db import models

# Create your models here.
class Subscription(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    location= models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    