from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date', 'likes']  # <-- add likes here
    list_filter = ['date']                           # optional: filter by date
    search_fields = ['photo']                         # optional: search by photo
