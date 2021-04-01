from django.db import models


# Create your models here.

class student_marks(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=200)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()

    class Meta:
        db_table = 'student_leaderboard'
