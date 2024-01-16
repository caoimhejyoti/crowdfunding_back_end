from rest_framework import serializers
from .models import Festival, Ticket, Pledge


class PledgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

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

    class Meta:
        model = Festival
        fields = "__all__"
    