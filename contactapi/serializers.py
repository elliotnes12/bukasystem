from rest_framework import serializers
from .models import Contact 

class ContactSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    email = serializers.EmailField()
    asunto = serializers.CharField()
    mensaje = serializers.CharField()

    def create(self,validate_data):
        instance = Contact()
        instance.name = validate_data.get('name')
        instance.email = validate_data.get('email')
        instance.asunto = validate_data.get('asunto')
        instance.mensaje = validate_data.get('mensaje')
        instance.save()
        return instance

