from django.db import models
from datetime import  datetime

# Create your models here.
class Blog(models.Model):

    categoryChoices = (
        ('Advance Programming','ADVANCE PROGRAMMING'),
        ('Basic Programming','BASIC PROGRAMMING'),
        ('Pattern Blog','PATTERN BLOG'),
    )


    blog_id = models.AutoField(primary_key=True)
    blog_image = models.ImageField(upload_to="images/blog",default=None,blank=True, null=True)
    blog_url = models.CharField(max_length=100,unique=True)
    blog_title = models.CharField(max_length=100,default=None,blank=True, null=True)
    blog_sub_title = models.CharField(max_length=100,default=None,blank=True, null=True)
    blog_des = models.TextField(default=None,blank=True, null=True)
    blog_ex1 = models.TextField(default=None,blank=True, null=True)
    blog_ex2 = models.TextField(default=None,blank=True, null=True)
    blog_python = models.TextField(default=None,blank=True, null=True)
    blog_c = models.TextField(default=None,blank=True, null=True)
    blog_cpp = models.TextField(default=None,blank=True, null=True)
    blog_java = models.TextField(default=None,blank=True, null=True)
    blog_category = models.CharField(max_length=50,default="",choices=categoryChoices)
    blog_status = models.CharField(max_length=20,default='Active')
    blog_date = models.DateTimeField(default=datetime.now())

    # def __str__(self):
    #     return self.contact_id
