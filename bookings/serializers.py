from rest_framework import serializers
from .models import Booking
from django.utils import timezone

class CreateRoomBookingSerializer(serializers.ModelSerializer):
    
    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests"
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now())
        if now > value:
            raise serializers.ValidationError("ERROR! Cannot book a past date.")
        return value
    
    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("ERROR! Cannot book a past date.")
        return value
    
    def validate(self, data):
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in time should be earlier than check out date"
            )
        return data

class PublicBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking,
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests"
        )