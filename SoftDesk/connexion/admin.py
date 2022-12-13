from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")


admin.site.register(models.User, UserAdmin)


class ContributeurAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "role", "projet")


admin.site.register(models.Contributeur, ContributeurAdmin)
