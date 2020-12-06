from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'author', 'name', 'begin_date', 'end_date']

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, event, validated_data):
        event.name = validated_data.get('name', event.name)
        event.begin_date = validated_data.get('begin_date', event.begin_date)
        event.end_date = validated_data.get('end_date', event.end_date)
        event.save()
        return event
