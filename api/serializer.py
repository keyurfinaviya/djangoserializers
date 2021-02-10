from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
	
	def start(value):
		if value[0] == value[0].lower():
			raise serializers.ValidationError('first letter should be capital')
 

	class Meta:

		model = Student
		fields = ['name','roll','city']
		


	# # id  = serializers.IntegerField()
	# name = serializers.CharField(max_length = 100, validators = [start])
	# roll = serializers.IntegerField()
	# city = serializers.CharField(max_length=100, validators = [start])

	# def create(self, validate_data):
	# 	return Student.objects.create(**validate_data)

	# def update(self, instance, validate_data):
	# 	instance.name = validate_data.get('name',instance.name)
	# 	instance.roll = validate_data.get('roll',instance.roll)
	# 	instance.city = validate_data.get('city',instance.city)
	# 	instance.save()
	# 	return instance

	
	

	def validate_roll(self, value):
		if value >= 200:
			raise serializers.ValidationError('Seats Full')
		return value
