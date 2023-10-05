from django.db import models

# Create your models here.


class Machine(models.Model):
    product = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    serialNumber = models.CharField(unique=True, max_length=25)
    machineTypeModel = models.CharField(max_length=16)
    biosVersion = models.CharField(max_length=16)
    biosReleaseDate = models.DateField()

    def __str__(self):
        return self.model


class DriveDisk(models.Model):
    driveName = models.CharField(max_length=25)
    serialNumber = models.CharField(max_length=25)
    Interface = models.CharField(max_length=25)
    diskLocationUnit = models.CharField(max_length=5)
    totalVolume = models.CharField(max_length=25)
    usedVolume = models.CharField(max_length=25)
    machine = models.ForeignKey(
        Machine, on_delete=models.SET_NULL, null=True, blank=True, default=None, max_length=25
    )


class BootboxDriveDisk(models.Model):
    diskLocationUnit = models.CharField(max_length=5)
    totalVolume = models.CharField(max_length=25)
    usedVolume = models.CharField(max_length=25)


class OsImage(models.Model):
    system = models.CharField(max_length=25)
    plataform = models.CharField(max_length=25)
    version = models.CharField(max_length=25)
    edition = models.CharField(max_length=25)
    size = models.CharField(max_length=25)
    lastUpdate = models.CharField(max_length=25)
    Language = models.CharField(max_length=25)
    bootbox = models.ForeignKey(
        BootboxDriveDisk, on_delete=models.SET_NULL, null=True, blank=True, default=None, max_length=25
    )
