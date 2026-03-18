from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *

def dashboard(request):
    total_rooms = LabRoom.objects.count()
    total_units = ComputerUnit.objects.count()
    total_inspections = Inspection.objects.count()

    # List of rooms with pagination (10 per page)
    rooms_qs = LabRoom.objects.all().order_by('room_name')

    paginator = Paginator(rooms_qs, 10)
    page_number = request.GET.get('page', 1)
    rooms = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {
        'total_rooms': total_rooms,
        'total_units': total_units,
        'total_inspections': total_inspections,
        'rooms': rooms,
    })


def room_detail(request, room_id):
    room = LabRoom.objects.get(id=room_id)
    units = ComputerUnit.objects.filter(room=room)

    return render(request, 'room_detail.html', {
        'room': room,
        'units': units
    })


def inspection_report(request):
    inspections = Inspection.objects.select_related(
        'unit', 'technician', 'period'
    ).all()

    return render(request, 'report.html', {
        'inspections': inspections
    })