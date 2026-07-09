from django.shortcuts import render


def appointment_list(request):

    return render(
        request,
        'appointments/appointment_list.html'
    )