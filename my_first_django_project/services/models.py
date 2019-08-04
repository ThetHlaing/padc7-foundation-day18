from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField('Name of the Service',max_length=250)
    description = models.TextField("Description of the service",blank=True)
    created_at = models.DateTimeField('Created Date')

    def __str__(self):
        return self.name