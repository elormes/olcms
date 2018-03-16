from django.contrib import admin
from videos.models import Video, Playlist, Tags, Category


admin.site.register(Playlist)
admin.site.register(Tags)
admin.site.register(Category)
admin.site.register(Video)
