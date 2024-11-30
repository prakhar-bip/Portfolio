from django.db import models


class contact_details(models.Model):
    Email = models.EmailField(unique= True)
    Contact_number = models.CharField(max_length=15)
    Name = models.CharField(max_length=150)
    Messages = models.TextField(max_length=1000)


    def __str__(self):
        return self.Name
    

class python_projects(models.Model):
    Project_name = models.CharField(max_length=100)
    Project_description = models.TextField(max_length=1000)
    Project_link = models.CharField(max_length=1000)
    Project_created_on = models.DateField()
    Project_technology = models.TextField(max_length= 250)


    def __str__(self):
        return self.Project_name