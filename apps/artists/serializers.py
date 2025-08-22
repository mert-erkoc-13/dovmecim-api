from rest_framework import serializers
from .models import ArtistProfile

class ArtistProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ArtistProfile
        fields = ('id', 'username', 'bio', 'location')