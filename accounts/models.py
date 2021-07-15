from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def is_teacher(self):
        """
        Checks if the user has superuser or staff status and 
        exists in the Teachers group.
        """
        return self.is_active and (
            self.is_superuser
            or self.is_staff
            and self.groups.filter(name="Teachers").exists()
        )

    
    @property
    def is_counselor(self):
        """
        Checks if the user has superuser or staff status and 
        exists in the Counselors group.
        """
        return self.is_active and (
            self.is_superuser
            or self.is_staff
            and self.groups.filter(name="Counselors").exists()
        )

    
    @property
    def is_headmaster(self):
        """
        Checks if the user has superuser or staff status and 
        exists in the Headmasters group.
        """
        return self.is_active and (
            self.is_superuser
            or self.is_staff
            and self.groups.filter(name="Headmaster").exists()
        )

    def __str__(self):
        return f'{self.name}'
