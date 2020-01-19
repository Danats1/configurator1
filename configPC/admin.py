from django.contrib import admin
from .models import PC,CPU,GPU,Power,RAM,Motherboard

admin.site.register(PC)
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(Power)
admin.site.register(RAM)
admin.site.register(Motherboard)