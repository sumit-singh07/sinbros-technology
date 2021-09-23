from django.db import models
from datetime import  datetime

# Create your models here.
class Portfolio(models.Model):


    statusChoices = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )

    portfolio_id = models.AutoField(primary_key=True)
    portfolio_image = models.ImageField(upload_to="images/portfolio",default=None,blank=True, null=True)
    portfolio_title = models.CharField(max_length=100,default=None,blank=True, null=True)
    portfolio_category = models.CharField(max_length=100,default=None,blank=True, null=True)
    portfolio_status = models.CharField(max_length=20,default='Active',choices=statusChoices)
    portfolio_date = models.DateTimeField(default=datetime.now())

    # def __str__(self):
    #     return self.contact_id
