from django.db import models
from django.utils import timezone

# Create your models here.

class Models(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('BT','BLACK TEA')
    ]
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/',default='chais/default.jpg')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE,default='ML')
    price = models.IntegerField(default=0)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name


