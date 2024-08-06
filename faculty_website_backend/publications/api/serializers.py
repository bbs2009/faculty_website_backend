# from rest_framework import serializers

# from faculty_website_backend.users.models import User


# class UserSerializer(serializers.ModelSerializer[User]):
#     class Meta:
#         model = User
#         fields = ["name", "url"]

#         extra_kwargs = {
#             "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
#         }


import base64
from rest_framework import serializers
from faculty_website_backend.publications.models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ['id', 'title', 'author', 'category', 'date', 'description', 'fileData', 'fileName', 'file']
        read_only_fields = ['fileData', 'fileName', 'file']

    def create(self, validated_data):
        # print(validated_data)
        file = validated_data.pop('file', None)
        instance = Publication.objects.create(**validated_data)
        
        if file:
            file_name = file.name
            # print(file_name)
            file_content = file.read()
            file_base64 = base64.b64encode(file_content).decode('utf-8')
            # print(file_base64)
            instance.fileName = file_name
            instance.fileData = file_base64
            instance.save()

        return instance

    def update(self, instance, validated_data):
        file = validated_data.pop('file', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if file:
            file_name = file.name
            file_content = file.read()
            file_base64 = base64.b64encode(file_content).decode('utf-8')

            instance.fileName = file_name
            instance.fileData = file_base64
        
        instance.save()
        return instance

    def get_file(self, obj):
        return {
            "fileName": obj.fileName,
            "fileData": obj.fileData
        } if obj.fileData and obj.fileName else None
