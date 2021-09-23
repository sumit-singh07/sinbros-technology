from django.db import models
from datetime import  datetime

# Create your models here.
class Learn(models.Model):

    categoryChoices = (
        ('Competitive Programming','COMPETITIVE PROGRAMMING'),
        ('Basic Programming','BASIC PROGRAMMING'),
        ('Pattern Programs','PATTERN PROGRAMS'),
    )

    statusChoices = (
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
    )

    learn_id = models.AutoField(primary_key=True)
    learn_image = models.ImageField(upload_to="images/learn",default=None,blank=True, null=True)
    learn_url = models.CharField(max_length=100,unique=True)
    learn_title = models.CharField(max_length=100,default=None,blank=True, null=True)
    learn_sub_title = models.CharField(max_length=100,default=None,blank=True, null=True)
    learn_des = models.TextField(default=None,blank=True, null=True)
    learn_ex1 = models.TextField(default=None,blank=True, null=True)
    learn_ex2 = models.TextField(default=None,blank=True, null=True)
    learn_python = models.TextField(default=None,blank=True, null=True)
    learn_c = models.TextField(default=None,blank=True, null=True)
    learn_cpp = models.TextField(default=None,blank=True, null=True)
    learn_java = models.TextField(default=None,blank=True, null=True)
    learn_category = models.CharField(max_length=50,default="",choices=categoryChoices)
    learn_sub_category = models.CharField(max_length=100,default=None,blank=True, null=True)
    learn_status = models.CharField(max_length=20,default='Active',choices=statusChoices)
    learn_date = models.DateTimeField(default=datetime.now())

    # def __str__(self):
    #     return self.contact_id
