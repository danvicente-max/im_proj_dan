from django.db import models

class LabRoom(models.Model):
    room_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Operational', 'Operational'), ('Maintenance', 'Maintenance')],
        default='Operational'
    )

    def __str__(self):
        return self.room_name


class ComputerUnit(models.Model):
    room = models.ForeignKey(LabRoom, on_delete=models.CASCADE)
    asset_tag = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.asset_tag


class Hardware(models.Model):
    unit = models.ForeignKey(ComputerUnit, on_delete=models.CASCADE)
    cpu = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    storage = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.unit} Hardware"


class Software(models.Model):
    unit = models.ForeignKey(ComputerUnit, on_delete=models.CASCADE)
    os = models.CharField(max_length=50)
    installed_apps = models.TextField()

    def __str__(self):
        return f"{self.unit} Software"


class Technician(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class AssessmentPeriod(models.Model):
    semester = models.CharField(max_length=20)
    school_year = models.CharField(max_length=20)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return f"{self.semester} {self.school_year}"


class Inspection(models.Model):
    unit = models.ForeignKey(ComputerUnit, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    period = models.ForeignKey(AssessmentPeriod, on_delete=models.CASCADE)
    date_checked = models.DateField()

    def __str__(self):
        return f"Inspection {self.id}"


class ConditionRating(models.Model):
    inspection = models.ForeignKey(Inspection, on_delete=models.CASCADE)
    hardware_condition = models.CharField(max_length=50)
    software_condition = models.CharField(max_length=50)
    remarks = models.TextField()

    def __str__(self):
        return f"Rating {self.id}"