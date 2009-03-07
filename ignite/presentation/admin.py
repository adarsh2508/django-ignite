from django.contrib import admin

from ignite.presentation.models import Presentation

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter_name', 'presenter_email')

admin.site.register(Presentation, PresentationAdmin)
