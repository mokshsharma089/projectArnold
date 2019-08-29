from django.db import models

# Create your models here.
class Games(models.Model):
    name=models.CharField(max_length=256)
    recommended=models.BooleanField(default=True)
    price=models.FloatField()
    description=models.TextField()
    image_url=models.URLField()
    trailer_id=models.CharField(max_length=20,default='GoyGlyrYb9c')
    def __str__(self):
        return self.name

class Offers(models.Model):
    game=models.ForeignKey(Games,on_delete=models.SET_NULL,null=True)
    rent=models.FloatField()
    time_period=models.PositiveSmallIntegerField()
    def __str__(self):
        return "{0} - {1} weeks".format(self.game.name,self.time_period)


    