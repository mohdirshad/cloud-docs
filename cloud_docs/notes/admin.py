from django.contrib import admin
from notes.models import Category, Tag, Note

class TagInline(admin.TabularInline):
    model = Tag
    extra = 1
    
class NoteAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    

admin.site.register(Category)
admin.site.register(Note, NoteAdmin)
admin.site.register(Tag)
