from django.contrib import admin
from . import models

class PhotoPostAdmin(admin.ModelAdmin):
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    #exclude = ('fullPhoto', 'thumbnailPhoto')

admin.site.register(models.PhotoPost, PhotoPostAdmin)
admin.site.register(models.Category)

# Register your models here.
