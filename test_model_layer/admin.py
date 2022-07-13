from django.contrib import admin

# Register your models here.
from test_model_layer.models import Runner


class RunnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'medal']

admin.site.register(Runner, RunnerAdmin)
