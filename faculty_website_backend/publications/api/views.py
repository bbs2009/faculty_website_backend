from rest_framework import status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from faculty_website_backend.publications.api.filters import PublicationFilterSet
from faculty_website_backend.publications.models import Publication
from .serializers import PublicationSerializer

class PublicationViewSet(GenericViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    pagination_class = PageNumberPagination
    filterset_class = PublicationFilterSet
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:   
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PublicationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PublicationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PublicationSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PublicationSerializer(instance, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)