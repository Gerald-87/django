from django.db import models

class Person(models.Model):
    """Abstract base model for common person attributes."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    """Model representing a teacher."""
    employee_id = models.CharField(max_length=10, unique=True)
    hire_date = models.DateField()
    specialization = models.CharField(max_length=100, blank=True, null=True)


class Subject(models.Model):
    """Model representing a subject."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="subjects")

    def __str__(self):
        return f"{self.name} ({self.code})"


class Class(models.Model):
    """Model representing a class (e.g., Grade 10)."""
    name = models.CharField(max_length=100, unique=True)
    teacher_in_charge = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="classes")
    subjects = models.ManyToManyField(Subject, related_name="classes")

    def __str__(self):
        return self.name


class Student(Person):
    """Model representing a student."""
    student_id = models.CharField(max_length=10, unique=True)
    enrollment_date = models.DateField()
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_id}"


class Parent(Person):
    """Model representing a parent."""
    children = models.ManyToManyField(Student, related_name="parents")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Attendance(models.Model):
    """Model representing attendance records."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[("Present", "Present"), ("Absent", "Absent")])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"


class Grade(models.Model):
    """Model representing grades for subjects."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grades")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grades")
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"


class SchoolEvent(models.Model):
    """Model representing a school event."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    participants = models.ManyToManyField(Student, related_name="events")

    def __str__(self):
        return self.name
