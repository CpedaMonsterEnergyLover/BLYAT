from django.contrib import admin
from .models import Liner
from .models import Cruise
from .models import Excursion

admin.site.register(Liner)
admin.site.register(Cruise)
admin.site.register(Excursion)