from django.db import models
from django.utils import timezone

# django provide by default user model for authentication
from django.contrib.auth.models import User


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
    

# One to Many

class ChaiReview(models.Model):
    chai = models.ForeignKey(Models,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
    
# many to many

class Stores(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(Models,related_name='stores')
    
    def __str__(self):
        return self.name

# one to one

class ChaiCertificates(models.Model):
    chai = models.OneToOneField(Models,on_delete=models.CASCADE,related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_untill = models.DateTimeField
    
    def __str__(self):
        return f'Certificate for {self.name.chai}'
