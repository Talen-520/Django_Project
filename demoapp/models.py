from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=30)
    price = models.IntegerField()
    
    def __str__(self):#more readable in shell
        return self.name

class Person_name (models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 

#one to many
#Menu category
#Menu 

class new_Menucategory(models.Model):
    menu_category_name = models.CharField(max_length=100)

class new_Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100, null=False)
    category_id = models.ForeignKey(new_Menucategory, on_delete=models.PROTECT, default=None) #first is table you connect to(foreign key) , second is what you do when you delete the table

