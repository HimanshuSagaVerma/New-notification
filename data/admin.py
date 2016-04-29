from django.contrib import admin

from data.models import notify
# Register your models here.

class notifyAdmin(admin.ModelAdmin):
	pass
admin.site.register(notify, notifyAdmin)
