from rest_framework import serializers
from .models import Student, Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['id','fname', 'lname', 'age', 'student_track']

class TrackSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['track_name']



# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ('fname', 'lname', 'age', 'student_track')
#         fields = '__all__'
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['student_track'] = instance.student_track.track_name
#         return data

# class TrackSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Track
#         fields = ('track_name',)
#         # fields = '__all__'