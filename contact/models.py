from django.db import models
from datetime import  datetime

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100)
    contact_mobile = models.CharField(max_length=20)
    contact_email = models.CharField(max_length=100)
    contact_sub = models.CharField(max_length=100)
    contact_msg = models.CharField(max_length=500)
    contact_status = models.CharField(max_length=20,default='Active')
    contact_date = models.DateTimeField(default=datetime.now())

    # def __str__(self):
    #     return self.contact_id
