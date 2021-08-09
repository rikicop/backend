from django.contrib import admin
from .models import Todo
from django_summernote.admin import SummernoteModelAdmin
 
#admin.site.register(Post)
 
class PostAdmin(SummernoteModelAdmin):
    list_display = ('foto', 'author', 'title','description','body')
    list_filter = ("title",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'author': ('title',)}
    summernote_fields = ('body','description')

admin.site.register(Todo,PostAdmin)
