from django.contrib import admin

from .models import DoctorProfile


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'specialization',
        'experience',
        'consultation_fee',
        'city',
    )

    search_fields = (
        'user__username',
        'hospital_name',
        'city',
        'specialization',
    )

    list_filter = (
        'specialization',
        'city',
    )


from .models import DoctorProfile, DoctorAvailability


@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):

    list_display = (
        'doctor',
        'day',
        'start_time',
        'end_time',
        'is_active',
    )

    list_filter = (
        'day',
        'is_active',
    )

    search_fields = (
        'doctor__user__username',
        'doctor__hospital_name',
    )