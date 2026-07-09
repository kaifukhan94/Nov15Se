from django.db import models
from django.conf import settings

class DoctorProfile(models.Model):
    from django.utils import timezone


    SPECIALIZATION_CHOICES = [

        ('Cardiologist', 'Cardiologist'),

        ('Dentist', 'Dentist'),

        ('Neurologist', 'Neurologist'),

        ('Orthopedic', 'Orthopedic'),

        ('Pediatrician', 'Pediatrician'),

        ('Dermatologist', 'Dermatologist'),

        ('General Physician', 'General Physician'),

    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    qualification = models.CharField(
        max_length=100
    )

    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES
    )

    experience = models.PositiveIntegerField(
        help_text="Experience in years"
    )

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    hospital_name = models.CharField(
        max_length=150
    )

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    bio = models.TextField()

    
    def __str__(self):

        return self.user.get_full_name() or self.user.username
    


class DoctorAvailability(models.Model):

    DAY_CHOICES = [

        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),

    ]

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.CASCADE,
        related_name='availabilities'
    )

    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = ['day', 'start_time']

    def __str__(self):

        return f"{self.doctor.user.get_full_name()} - {self.day} ({self.start_time} - {self.end_time})"