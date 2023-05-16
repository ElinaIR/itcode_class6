from django.db import models


class Employee(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronym = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.last_name


class Post(models.Model):
    name = models.CharField(max_length=50)
    duties = models.TextField()

    def __str__(self):
        return self.name

