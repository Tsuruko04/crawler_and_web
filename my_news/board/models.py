from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=20,default='')
    source = models.CharField(max_length=10,default='')
    content = models.CharField(max_length=2000)
    pic1 = models.CharField(max_length=50,default='')
    pic2 = models.CharField(max_length=50,default='')
    pic3 = models.CharField(max_length=50,default='')
    pic4 = models.CharField(max_length=50,default='')
    pic5 = models.CharField(max_length=50,default='')
    key1 = models.CharField(max_length=10,default='')
    key2 = models.CharField(max_length=10,default='')
    key3 = models.CharField(max_length=10,default='')
    def split(self):
        contentlist=self.content.split()
        return contentlist

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.CharField(max_length=20)
    content = models.CharField(max_length=500)