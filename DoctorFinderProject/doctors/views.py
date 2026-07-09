from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import DoctorProfileForm
from .models import DoctorProfile
from .availability_forms import DoctorAvailabilityForm
from .models import DoctorProfile, DoctorAvailability

@login_required
def create_doctor_profile(request):

    # Only doctors can create profiles
    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    # Prevent multiple profiles
    if DoctorProfile.objects.filter(user=request.user).exists():
        return redirect('doctor_dashboard')

    if request.method == "POST":

        form = DoctorProfileForm(request.POST)

        if form.is_valid():

            doctor = form.save(commit=False)

            doctor.user = request.user

            doctor.save()

            return redirect('doctor_dashboard')

    else:

        form = DoctorProfileForm()

    return render(
        request,
        'doctors/doctor_profile.html',
        {
            'form': form
        }
    )


@login_required
def doctor_dashboard(request):

    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    doctor = DoctorProfile.objects.get(
        user=request.user
    )

    return render(
        request,
        'doctors/doctor_dashboard.html',
        {
            'doctor': doctor
        }
    )



def doctor_list(request):

    doctors = DoctorProfile.objects.select_related('user').all()

    name = request.GET.get('name')

    specialization = request.GET.get('specialization')

    city = request.GET.get('city')

    if name:

        doctors = doctors.filter(

            user__first_name__icontains=name

        ) | doctors.filter(

            user__last_name__icontains=name

        )

    if specialization:

        doctors = doctors.filter(

            specialization=specialization

        )

    if city:

        doctors = doctors.filter(

            city__icontains=city

        )

    context = {

        'doctors': doctors,

        'name': name,

        'specialization': specialization,

        'city': city,

        'specializations': DoctorProfile.SPECIALIZATION_CHOICES,

    }

    return render(

        request,

        'doctors/doctor_list.html',

        context

    )



def doctor_detail(request, pk):

    doctor = get_object_or_404(
        DoctorProfile,
        pk=pk
    )

    return render(
        request,
        'doctors/doctor_detail.html',
        {
            'doctor': doctor
        }
    )



@login_required
def add_availability(request):

    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    if request.method == 'POST':

        form = DoctorAvailabilityForm(request.POST)

        if form.is_valid():

            availability = form.save(commit=False)

            availability.doctor = doctor

            availability.save()

            return redirect('doctor_dashboard')

    else:

        form = DoctorAvailabilityForm()

    return render(
        request,
        'doctors/add_availability.html',
        {
            'form': form
        }
    )



@login_required
def availability_list(request):

    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    availabilities = DoctorAvailability.objects.filter(
        doctor=doctor
    ).order_by('day', 'start_time')

    return render(
        request,
        'doctors/availability_list.html',
        {
            'availabilities': availabilities
        }
    )



@login_required
def edit_availability(request, pk):

    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    availability = get_object_or_404(
        DoctorAvailability,
        pk=pk,
        doctor=doctor
    )

    if request.method == "POST":

        form = DoctorAvailabilityForm(
            request.POST,
            instance=availability
        )

        if form.is_valid():

            form.save()

            return redirect('availability_list')

    else:

        form = DoctorAvailabilityForm(
            instance=availability
        )

    return render(
        request,
        'doctors/add_availability.html',
        {
            'form': form
        }
    )



@login_required
def delete_availability(request, pk):

    if request.user.role != 'DOCTOR':
        return redirect('dashboard')

    doctor = get_object_or_404(
        DoctorProfile,
        user=request.user
    )

    availability = get_object_or_404(
        DoctorAvailability,
        pk=pk,
        doctor=doctor
    )

    availability.delete()

    return redirect('availability_list')