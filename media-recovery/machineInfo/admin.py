from django.contrib import admin

from .models import DriveDisk, Machine


# Register your models here.
class MachineAdmin(admin.ModelAdmin):
    ...


@admin.register(DriveDisk)
class DriveDiskAdmin(admin.ModelAdmin):
    ...


admin.site.register(DriveDisk, DriveDiskAdmin)
