
from rest_framework import serializers

from django.contrib.auth.models import User

from bookings.models import Appointment

from datetime import datetime

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]

class AppointmentSerializer(serializers.ModelSerializer):

    doctor = serializers.StringRelatedField()

    class Meta:

        model = Appointment

        fields = "__all__"

        read_only_fields = ["id","token_number","appointment_time","created_at"]


    def validate(self, validated_data):

        appointment_date = validated_data.get("appointment_date")

        doctor = validated_data.get("doctor")

        phone_number = validated_data.get("phone")

        if appointment_date < datetime.today().date():

            raise serializers.ValidationError("invalid date , date should be  > current date")


        last_appointment_obj = Appointment.objects.filter(doctor=doctor,appointment_date=appointment_date).last()

        if last_appointment_obj:

            if last_appointment_obj.token_number == 3:

                raise serializers.ValidationError("bookings already full")

        return validated_data

    