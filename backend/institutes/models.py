from django.db import models

class Periods(models.Model):
    period = models.IntegerField(primary_key=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

class TimeSlot(models.Model):
    day = models.CharField(max_length=20)
    period = models.ForeignKey(Periods, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} {self.period}"

class Building(models.Model):
    building = models.CharField(max_length=200)

class Room(models.Model):
    room_no = models.CharField(max_length= 200)
    building_name = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=20, choices=[
        ('class', 'Class'), ('lab', 'Lab'), ('smartClass', 'Smart Class')
    ])
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.building_name} {self.room_no}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["room_no", "building_name"], 
                name="unique_roomno_building"
            )
        ]

class Department(models.Model):
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_type = models.CharField(max_length=10, choices=[
        ('major', 'Major'), ('minor', 'Minor'), ('elective', 'Elective')
    ])
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department} {self.course_name}"

class Subject(models.Model):
    subject_code = models.CharField(max_length=20, primary_key=True)
    subject_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_theory_hours = models.IntegerField()
    total_practical_hour = models.IntegerField()

    def __str__(self):
        return f"{self.subject_code} {self.subject_name}"

class Faculty(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    faculty_name = models.CharField(max_length=200)
    qualifications = models.CharField(max_length=1200)

    def __str__(self):
        return self.faculty_name

class FacultyUnavailability(models.Model):    
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    reason = models.CharField(max_length=1200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.faculty} unavailable at {self.timeslot.day} {self.timeslot.period}"

class Student(models.Model):
    enrollment_no = models.CharField(max_length=50, primary_key=True)
    student_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.enrollment_no} {self.student_name}"

# Relation ship models