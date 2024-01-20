from rest_framework import serializers
from .models import Festival, Ticket, Pledge


class PledgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous',instance.anonymous)
        instance.ticket_option = validated_data.get('ticket_option', instance.ticket_option)
        instance.festival = validated_data.get('festival', instance.festival)
        instance.supporter = validated_data.get('supporter', instance.supporter)
        instance.save()
        return instance
    class Meta:
        model = Pledge
        fields = "__all__"
class TicketSerializer(serializers.ModelSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    class Meta:
        model = Ticket
        fields = "__all__"
class FestivalSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Festival
        fields = "__all__"

class FestivalDetailSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    pledges = PledgeSerializer(many=True, read_only=True) 
    owner = serializers.ReadOnlyField(source='owner.id')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance



    class Meta:
        model = Festival
        fields = "__all__"
    