from django.db import models

from user.models import User


CHOICES_TASK = (
    ('yes', 'Yes'),
    ('no', 'No'))


class Note(models.Model):
    date = models.DateField(
        auto_now=True,
        verbose_name='Date',
        help_text='Current save date.')
    end_date = models.DateField(
        verbose_name='End date',
        help_text='Enter the end date.')
    note = models.TextField(
        verbose_name='Note',
        help_text='Enter the note.')
    attached = models.FileField(
        upload_to='attacheds/',
        verbose_name='Attached',
        help_text='Enter the attached.',
        null=True,
        blank=True)
    users = models.ManyToManyField(
        User,
        verbose_name='Users',
        help_text='Enter the users.',
        blank=True)
    task = models.CharField(
        max_length=10,
        choices=CHOICES_TASK,
        verbose_name="Task",
        help_text="Is a task?")
    tags = models.TextField(
        verbose_name='Tags',
        help_text='Enter the tags separated by comma.')
    type_field = models.CharField(
        max_length=150,
        verbose_name="Type",
        help_text="Enter the note's type.")