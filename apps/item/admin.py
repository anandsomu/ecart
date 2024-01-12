from django.contrib import admin
from apps.item import models


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "created")
    search_fields = ("name",)


admin.site.register(models.Item, ItemAdmin)
