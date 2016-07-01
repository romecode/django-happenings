from __future__ import unicode_literals

from django.contrib import admin
from happenings.models import Event, Location, Category, Tag, Cancellation


class CancellationInline(admin.TabularInline):
    model = Cancellation
    extra = 0


class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('start_date', 'end_date', 'all_day', 'title', 'description_short','description','banner','image',
                       'created_by',)
        }),
        ('Location', {
            'classes': ('collapse',),
            'fields': ('location',)
        }),
#         ('Category', {
#             'classes': ('collapse',),
#             'fields': ('categories',)
#         }),
#         ('Tag', {
#             'classes': ('collapse',),
#             'fields': ('tags',)
#         }),
#         ('Color', {
#             'classes': ('collapse',),
#             'fields': (
#                 ('background_color', 'background_color_custom'),
#                 ('font_color', 'font_color_custom'),
#             )
#         }),
    )

    list_display = ('admin_thumb','title', 'start_date', 'end_date')
    list_filter = ['start_date']
    search_fields = ['title']
    date_hierarchy = 'start_date'
    inlines = [CancellationInline]

admin.site.register(Event, EventAdmin)
admin.site.register(Cancellation)
admin.site.register(Location)
