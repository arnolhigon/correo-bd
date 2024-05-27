from django.db import models

from django.db import models

class Email(models.Model):
    subject = models.CharField(max_length=255)
    sender = models.CharField(max_length=255)
    date = models.DateTimeField()
    zip_file = models.FileField(upload_to='emails/', null=True, blank=True)