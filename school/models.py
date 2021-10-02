from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL


class Subject(models.Model):
    """
    Name and description of the subject.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=120, blank=True)

    def __str__(self):
        return self.name

class Grade(models.Model):
    GRADE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('F', 'F'),
        ('U', 'Unassigned')
    )
    student = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="grades")
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE, related_name="grades")
    grade = models.CharField(max_length=4, choices=GRADE_CHOICES, default='U')

    def __str__(self):
        return self.student.name
    
class Advice(models.Model):
    student = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="advices")
    advice = models.TextField(max_length=240)

    def __str__(self):
        return f"Advice for {self.student.name}"
    