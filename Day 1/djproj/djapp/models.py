from django.db import models

# Create your models here.

class Track(models.Model):
    track_name = models.CharField(max_length=50)
    def __str__(self):
        return self.track_name

class Student(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, default='NoName')
    age = models.IntegerField(default=0)
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.fname + " " + self.lname
    def is_adult(self):
        return self.age >= 15
    is_adult.short_description = 'Graduated Student'
    is_adult.boolean = True