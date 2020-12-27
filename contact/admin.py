from django.contrib import admin
from contact import models

class ContactFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

admin.site.register(models.ContactFeedback, ContactFeedbackAdmin)
