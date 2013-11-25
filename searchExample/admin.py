from django.contrib import admin
from searchExample.models import Note, NoteSegment, UserProfile, SaveThisSearch

#admin.site.register(Note)

class NoteAdmin(admin.ModelAdmin):
    search_fields = ('header',)

admin.site.register(Note, NoteAdmin)

class NoteSegmentAdmin(admin.ModelAdmin):
    search_fields = ('body',),
    
admin.site.register(NoteSegment, NoteSegmentAdmin)

admin.site.register(UserProfile)
admin.site.register(SaveThisSearch)