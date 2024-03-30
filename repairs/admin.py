from django.contrib import admin

from repairs.models import Repair, Works, RepairType, Parts, Locomotive, PlacesToWork

admin.site.register(Repair)
admin.site.register(Works)
admin.site.register(RepairType)
admin.site.register(Parts)
admin.site.register(Locomotive)
admin.site.register(PlacesToWork)
