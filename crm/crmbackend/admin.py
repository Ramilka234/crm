from django.contrib import admin

from .models import Users, Roles, Houses, House_Photos

admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Houses)
admin.site.register(House_Photos)