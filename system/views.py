from django.core.paginator import Paginator
from django.shortcuts import render, redirect
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


def inspection_form(request):

    rooms = LabRoom.objects.all()

    if request.method == "POST":

        room_id = request.POST.get("room")
        asset_tag = request.POST.get("asset_tag")
        condition = request.POST.get("condition")
        remarks = request.POST.get("remarks")

        room = LabRoom.objects.get(id=room_id)

        unit = ComputerUnit.objects.create(
            room=room,
            asset_tag=asset_tag,
            status=condition
        )

        inspection = Inspection.objects.create(
            unit=unit,
            technician=Technician.objects.first(),
            period=AssessmentPeriod.objects.first(),
            date_checked=date.today()
        )

        ConditionRating.objects.create(
            inspection=inspection,
            hardware_condition=condition,
            software_condition=condition,
            remarks=remarks
        )

        return redirect("dashboard")

    return render(request, "inspection.html", {
        "rooms": rooms
    })

def laboratory(request):
    rooms_qs = LabRoom.objects.all().order_by('room_name')
    paginator = Paginator(rooms_qs, 10)
    page_number = request.GET.get('page', 1)
    rooms = paginator.get_page(page_number)
    return render(request, 'laboratory.html', {
        'rooms': rooms,
    })

def report(request):
    rooms_qs = LabRoom.objects.all().order_by('room_name')

    paginator = Paginator(rooms_qs, 10)
    page_number = request.GET.get('page', 1)
    rooms = paginator.get_page(page_number)

    return render(request, 'report.html', {
        'rooms': rooms,
    })

def add_lab(request):

    if request.method == "POST":

        room_name = request.POST.get("room_name")
        location = request.POST.get("location")
        capacity = request.POST.get("capacity")

        LabRoom.objects.create(
            room_name=room_name,
            location=location,
            capacity=capacity
        )

    return redirect("dashboard")

def delete_lab(request, room_id):
    room = LabRoom.objects.get(id=room_id)
    room.delete()
    return redirect("laboratory")

def add_unit(request):

    if request.method == "POST":

        asset_tag = request.POST.get("asset_tag")
        room_id = request.POST.get("room_id")

        room = LabRoom.objects.get(id=room_id)

        ComputerUnit.objects.create(
            asset_tag=asset_tag,
            room=room
        )

    return redirect("laboratory")

def delete_unit(request, unit_id):
    unit = ComputerUnit.objects.get(id=unit_id)
    unit.delete()
    return redirect("laboratory")