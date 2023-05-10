from django.db import models

class userdetail(models.Model):
    username=models.CharField(max_length=100)
    useremail=models.EmailField(max_length=100)
    userimage=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.username 

class bogdetail(models.Model):
        blogtitle=models.CharField(max_length=100)
        blogimage=models.ImageField(upload_to='images/')
        blogdesc=models.CharField(max_length=1000)
        blogdate=models.DateTimeField(auto_now_add=True)
        blogcontact=models.IntegerField()

        def __str__(self):
             return self.blogtitle 
 