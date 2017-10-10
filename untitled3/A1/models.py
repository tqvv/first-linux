from django.db import models
play =(
    ('Y','play'),
    ('N','not play'),
)
# Create your models here.
class Stream(models.Model):
    name = models.CharField(max_length=100)
    head_img = models.FileField(upload_to='./upload',default='null')
    price = models.IntegerField(default=1)
    play = models.CharField(max_length=100,choices=play,default='N')
