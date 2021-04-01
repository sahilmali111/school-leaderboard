from rest_framework import serializers
from .models import student_marks

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student_marks
        fields = "__all__"