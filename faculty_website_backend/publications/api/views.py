from rest_framework import status, permissions
# from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from faculty_website_backend.publications.models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(GenericViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    pagination_class = PageNumberPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:   
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    
    def list(self, request, *args, **kwargs):
        queryset = self.paginate_queryset(Publication.objects.all())
        serializer = PublicationSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)
    

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


    
    def search(self, request, *args, **kwargs):
        query = request.query_params.get('q', None)
        if query is not None:
            queryset = Publication.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = PublicationSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = PublicationSerializer(queryset, many=True)
            return Response(serializer.data)
        return Response({"detail": "No query provided."}, status=status.HTTP_400_BAD_REQUEST)





# from rest_framework import status
# from rest_framework.decorators import action
# from rest_framework.mixins import ListModelMixin
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.response import Response
# from rest_framework.viewsets import GenericViewSet

# from faculty_website_backend.users.models import User

# from .serializers import UserSerializer


# class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "pk"

#     def get_queryset(self, *args, **kwargs):
#         assert isinstance(self.request.user.id, int)
#         return self.queryset.filter(id=self.request.user.id)

#     @action(detail=False)
#     def me(self, request):
#         serializer = UserSerializer(request.user, context={"request": request})
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

# from rest_framework import generics
# from rest_framework import status
# from rest_framework.mixins import ListModelMixin
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.mixins import DestroyModelMixin
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.response import Response
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.pagination import PageNumberPagination
# from faculty_website_backend.publications.models import Publication
# from .serializers import PublicationSerializer

#I need create, retrieve, list, update, and delete functionality for the Publication model
#list, retrive without any authentication
#update, delete, create with authentication

# class PublicationViewSet(GenericViewSet):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#     pagination_class = PageNumberPagination

#     def list(self, request, *args, **kwargs):
#         queryset = Publication.objects.all()
#         serializer = PublicationSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = PublicationSerializer(instance)
#         return Response(serializer.data)

#     def create(self, request, *args, **kwargs):
#         serializer = PublicationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = PublicationSerializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# class PublicationViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#     pagination_class = PageNumberPagination



# class PublicationCreateAPIView(generics.CreateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#     pagination_class = PageNumberPagination
#     permissions = [permissions.IsAuthenticated]
        
    

# class PublicationRetrieveUpdateDestroyAPIView(generics.CreateAPIView):
#     queryset = Publication.objects.all()
#     serializer_class = PublicationSerializer
#     pagination_class = PageNumberPagination
