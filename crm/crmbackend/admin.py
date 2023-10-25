from django.contrib import admin

from .models import Users, Roles, Houses

admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Houses)