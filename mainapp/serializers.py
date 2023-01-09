from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
	name=serializers.CharField(required=False, allow_blank=True, max_length=100)
	from_email=serializers.EmailField()
	subject=serializers.CharField(required=False, allow_blank=True, max_length=100)
	body=serializers.CharField(required=False, allow_blank=True, max_length=500)
	files=serializers.FileField(required=False, max_length=100000, allow_empty_file=False, use_url=False)
	to_email=serializers.EmailField()