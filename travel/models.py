from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Workingtravel(models.Model):
    name=models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='work')
    image = models.ImageField(upload_to='images' , null=True)
    


    def __str__(self):
        return self.name



