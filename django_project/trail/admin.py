from django.contrib.gis import admin
from trail.models.trail import Trail

class TrailAdmin(admin.ModelAdmin):
    """Trail admin model."""

    list_display = ['name', 'colour', 'offset']
    search_fields = ('name', 'colour', 'offset',)
    list_filter = ('name', 'colour', 'offset',)
    list_per_page = 10

    def queryset(self, request):
        """Ensure we use the correct manager.
        :param request: HttpRequest object
        """

        query_set = self.model.objects
        ordering = self.get_ordering(request)
        if ordering:
            query_set = query_set.order_by(*ordering)
        return query_set

admin.site.register(Trail, TrailAdmin)
