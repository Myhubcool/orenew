from django.contrib import admin
from .models import usermodel, rtlrmodel, all
admin.site.register(usermodel)
admin.site.register(rtlrmodel)
admin.site.register(all)

