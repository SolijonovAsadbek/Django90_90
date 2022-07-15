from django.contrib import admin

# Register your models here.
from test_model_layer.models import Runner, Person, Group, Membership, Publication, Article, Place, Restaurant, Waiter


class RunnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'medal']

admin.site.register(Runner, RunnerAdmin)
admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)