from django.db import models

# Create your models here.
class dbtest(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    content=models.TextField()
    url=models.URLField()
    email=models.EmailField()
    cdate=models.DateTimeField(auto_now_add=True)
