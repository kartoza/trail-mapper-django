from django.contrib.gis import admin

from .models.trail import Trail
from .models.trail_section import TrailSection
from .models.grade import Grade
from .models.trail_sections import TrailSections
from .models.category import Category
from .models.point_of_interest import PointOfInterest


class TrailAdmin(admin.ModelAdmin):
    """Trail admin model."""

    list_display = [
        'guid',
        'name',
        'offset',
        'geom'
    ]
    search_fields = (
        'guid',
        'name',
        'offset',
    )
    list_filter = (
        'guid',
        'name',
        'offset',
    )
    list_per_page = 10

    prepopulated_fields = {'slug': ('name',),}

    def queryset(self, request):
        """Ensure we use the correct manager.
        :param request: HttpRequest object
        """

        query_set = self.model.objects
        ordering = self.get_ordering(request)
        if ordering:
            query_set = query_set.order_by(*ordering)
        return query_set


class TrailSectionAdmin(admin.ModelAdmin):
    """Trail section model admin."""
    list_display = ['guid', 'name', 'image', 'time_start', 'time_end']
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 10

    prepopulated_fields = {'slug': ('name',), }

    def queryset(self, request):
        """Ensure we use the correct manager.
        :param request: HttpRequest object
        """

        query_set = self.model.objects
        ordering = self.get_ordering(request)
        if ordering:
            query_set = query_set.order_by(*ordering)
        return query_set



class GradeAdmin(admin.ModelAdmin):
    """Grade section model admin."""

    list_display = ['guid', 'name', 'image']
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 10

    prepopulated_fields = {'slug': ('name',), }

    def queryset(self, request):
        """Ensure we use the correct manager.
        :param request: HttpRequest object
        """

        query_set = self.model.objects
        ordering = self.get_ordering(request)
        if ordering:
            query_set = query_set.order_by(*ordering)
        return query_set


class TrailSectionsAdmin(admin.ModelAdmin):
    """Trail Sections model admin."""

    list_display = ['order']
    search_fields = ('order',)
    list_filter = ('order',)
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



class CategoryAdmin(admin.ModelAdmin):
    """Category model admin."""

    list_display = ['guid', 'name']
    search_fields = ('name',)
    list_filter = ('name',)
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



class POIAdmin(admin.ModelAdmin):
    """Category model admin."""

    list_display = ['guid', 'name', 'image']
    search_fields = ('name',)
    list_filter = ('name',)
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
admin.site.register(TrailSection, TrailSectionAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(TrailSections, TrailSectionsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PointOfInterest, POIAdmin)
