from rest_framework import serializers

from .models import TimeStamp

class TimeStampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeStamp
        fields = ('timestamp',)