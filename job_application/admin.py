from django.contrib import admin

from .models import Form 


class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('-first_name', ) #minus orders it in reverse
    readonly_fields = ('occupation', )


admin.site.register(Form, FormAdmin)
