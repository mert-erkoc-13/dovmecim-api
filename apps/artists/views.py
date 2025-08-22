from rest_framework import viewsets
from .models import ArtistProfile
from .serializers import ArtistProfileSerializer

class ArtistProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer