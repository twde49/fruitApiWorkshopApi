from django.contrib import admin

from workshopApi.models import Color, Fruit, Season, CustomUser, Platform, Client

# Register your models here.
admin.site.register(Color)
admin.site.register(Fruit)
admin.site.register(Season)
admin.site.register(CustomUser)
admin.site.register(Platform)
admin.site.register(Client)
