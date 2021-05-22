from django.db import models

# Create your models here.
class feedback(models.Model):
    pname = models.CharField(max_length=25)
    pemail = models.CharField(max_length=25, default="NA")
    psugg = models.TextField(max_length=1000)
    class Meta:
        db_table = 'feedback'
    def __str__(self):
        return self.pname    