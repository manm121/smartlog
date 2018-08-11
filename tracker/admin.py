from django.contrib import admin
from tracker.models import *

# Register your models here.
admin.site.register(Store)
admin.site.register(CallType)
admin.site.register(CallSubType)
admin.site.register(CallerType)
admin.site.register(ServiceLocation)
admin.site.register(Request)
admin.site.register(RequestProgress)