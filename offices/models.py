from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=55, unique=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.slug


class Employee(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = 'email'

    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        null=True, on_delete=models.SET_NULL,
        related_name='employees'
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
