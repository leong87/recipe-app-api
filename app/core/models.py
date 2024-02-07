
""" Database models"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


# define user manadander base on BaseUserManager
class UserManager(BaseUserManager):
    """Manager for users"""

    # provide min fields to create user /  extra_field to provide extra fields needed  by child class
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        # normalize email is implemente and test to make sure it works properly
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email, **extra_fields))
        user.set_password(password)
        user.save(using=self._db)

        return user


# AbstractBaseUser has funtionality authentification system
# PermissionsMixin has funtionality permision feature oif django and filed form permision
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    # only staff user will be able to load into the admin
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # I replace the default username field for tje custom email field.
    USERNAME_FIELD = "email"
