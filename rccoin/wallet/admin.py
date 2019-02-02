from django.contrib import admin
from .models import Cancellation

# Register your models here.

class CancellationAdmin(admin.ModelAdmin):
    model = Cancellation
    list_display = ['s_id', 'txHash',]
    verbose_name_plural = 'Cancellation'

admin.site.register(Cancellation, CancellationAdmin)
