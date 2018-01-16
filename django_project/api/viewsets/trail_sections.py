from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import TrailSectionsSerializer
from trail_mapper.models import TrailSections, Trail


class TrailSectionsViewSet(viewsets.ModelViewSet):
    """This is the m2m join of trails and trail_sections."""
    queryset = TrailSections.objects.all()
    serializer_class = TrailSectionsSerializer
    lookup_field = 'guid'

    def list(self, request, *args, **kwargs):
        #recreate the queryset here so it has all data
        sections_queryset = TrailSections.objects.all()
        trail_queryset = Trail.objects.all()
        trails = []
        for trail in trail_queryset:
            trail_sections = sections_queryset.filter(trail__guid=trail.guid)
            trail_sections_list = []
            for trail_section in trail_sections:
                trail_sections_list.append(trail_section.trail_section.guid)
            trail_dict = {
                'trail_guid': trail.guid,
                'trail_section_guids': trail_sections_list
            }
            trails.append(trail_dict)

        content = {
            "trails_with_sections": trails
        }

        return Response(content)
