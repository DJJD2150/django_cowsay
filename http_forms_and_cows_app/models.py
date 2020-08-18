from django.db import models

# Create your models here.
# Got help from Sohail Aslam in study hall here
class CowsayModel(models.Model):
    cowsay = models.CharField(max_length=120)

    def __str__(self):
        return self.cowsay
