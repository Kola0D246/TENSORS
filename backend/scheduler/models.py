from django.db import models
from institutes.models import TimeSlot, Room, Faculty, Subject, Student

class Occupancy(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('booked', 'Booked'), ('blocked', 'Blocked')])

    class Meta:
        unique_together = ('room', 'timeslot')
