from django.contrib import admin
from .models import Post, PostTranslation


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['title', 'timestamp']
    list_display = ['title', 'description', 'timestamp']
    list_editable = ['description']
    readonly_fields = ['timestamp']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(PostTranslation)
