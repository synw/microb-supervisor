# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Instance


@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("domain", "ip")}
    search_fields = ['ip', 'domain']
    list_display = ["domain", "ip", "port"]
    readonly_fields = ["url", "channel_in", "channel_out"]