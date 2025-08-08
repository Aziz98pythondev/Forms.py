from django.db import models

class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'AboutUs'

    def __str__(self):
        return self.name