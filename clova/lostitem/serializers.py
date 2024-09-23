from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Lost
from accounts.serializers import UserSerializer

class LostSerializer(serializers.ModelSerializer):
    lostid = serializers.IntegerField(source='id', read_only=True)
    lostdate = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', required=False)
    losttime = serializers.TimeField(input_formats=['%H'], format='%H', required=False)
    userget = UserSerializer(source='user.username', read_only=True)

    class Meta:
        model = Lost
        fields = ['lostid', 'image', 'lostdate', 'losttime', 'description', 'moredesc', 'founded', 
                  'userget', 'category', 'getwhere', 'nowwhere']

class LostlistSerializer(serializers.ModelSerializer):
    lostid = serializers.IntegerField(source='id', read_only=True)
    lostdate = serializers.DateField(input_formats=['%Y-%m-%d'], format='%Y-%m-%d', required=False)

    class Meta:
        model = Lost
        fields = ['lostid', 'image', 'category', 'getwhere', 'lostdate']