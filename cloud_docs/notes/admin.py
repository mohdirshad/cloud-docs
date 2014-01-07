from django.contrib import admin
from notes.models import Category, Tag, Note


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
    
class TagInline(admin.TabularInline):
    model = Tag
    extra = 1
    
class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
