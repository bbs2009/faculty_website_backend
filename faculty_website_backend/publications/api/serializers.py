from rest_framework import serializers
from faculty_website_backend.publications.models import Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'author', 'category', 'date', 'description', 'file']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Publication.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.category = validated_data.get('category', instance.category)
        instance.date = validated_data.get('date', instance.date)
        instance.description = validated_data.get('description', instance.description)

        file = validated_data.get('file', None)
        if file:
            instance.file = file

        instance.save()
        return instance