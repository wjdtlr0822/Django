from django.db import models

# Create your models here.
class loldb(models.Model):
    name=models.CharField(max_length=100)     #롤 닉네임

    team_tier=models.CharField(max_length=100,default='0')   #롤 티어
    team_rank=models.CharField(max_length=100,default='0')        #티어 몇
    team_point=models.IntegerField(default=0)
    team_win=models.IntegerField(default=0)
    team_loss=models.IntegerField(default=0)

    solo_tier=models.CharField(max_length=100,default='0')
    solo_rank=models.CharField(max_length=100,default='0')
    solo_point=models.IntegerField(default=0)
    solo_win = models.IntegerField(default=0)
    solo_loss = models.IntegerField(default=0)

    def __str__(self):
        return self.name