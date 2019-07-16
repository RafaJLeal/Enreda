from django.db import models

class User(models.Model):
    name = models.CharField(
        max_length=153,
        verbose_name="User's name",
        help_text="Enter the user's name.")
    email = models.EmailField(
        verbose_name="Email's name",
        help_text="Enter the email's name.")
