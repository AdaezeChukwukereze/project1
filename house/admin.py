from django.contrib import admin
from .models import Estate


class EstateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("address",)}

admin.site.register(Estate, EstateAdmin)
