from django.contrib import admin
# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count_text']
    list_display_links = ['title']

    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))
    count_text.short_description = 'text 글자 수'

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)