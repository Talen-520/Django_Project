from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Person_name)
admin.site.register(models.new_Menucategory)
admin.site.register(models.new_Menu)
admin.site.register(models.Menu)

#register model
from .models import Logger
admin.site.register(Logger)

from .models import Reservation
admin.site.register(Reservation)

from .models import survey
admin.site.register(survey)

from .models import userinformation
admin.site.register(userinformation)