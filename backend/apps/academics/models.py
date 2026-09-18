from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='programs',
    )

    def __str__(self):
        return self.code


class Semester(models.Model):
    number = models.PositiveSmallIntegerField(
    validators=[
        MinValueValidator(1),
        MaxValueValidator(8),
    ]
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name='semesters',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['program', 'number'],
                name='unique_program_semester',
            )
        ]
        ordering = ['number']

    def __str__(self):
        return f"{self.program.code} - Semester {self.number}"