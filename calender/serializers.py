from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "date", "fav", "active", "startField", "endField")

        def update(self, instance, validated_data):
            instance.id = validated_data.get("id", instance.id)
            instance.title = validated_data.get("title", instance.title)
            instance.date = validated_data.get("date", instance.date)
            instance.fav = validated_data.get("fav", instance.fav)
            instance.active = validated_data.get("active", instance.active)
            instance.startField = validated_data.get("startField", instance.startField)
            instance.endField = validated_data.get("endField", instance.endField)
            instance.save()
            return instance


class EventListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.title = validated_data.get("title", instance.title)
        instance.date = validated_data.get("date", instance.date)
        instance.fav = validated_data.get("fav", instance.fav)
        instance.active = validated_data.get("active", instance.active)
        instance.startField = validated_data.get("startField", instance.startField)
        instance.endField = validated_data.get("endField", instance.endField)
        instance.save()
        return instance

    class Meta:
        model = Event
        fields = ("id", "title", "date", "fav", "active", "startField", "endField")
