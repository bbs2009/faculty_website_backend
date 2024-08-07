from django_filters import rest_framework as filters
# from django_filters.rest_framework import DjangoFilterBackend

from faculty_website_backend.publications.models import Publication

class PublicationFilterSet(filters.FilterSet):

	title = filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
        label="Title Contains",
    )
     
	published_from = filters.DateFilter(
        field_name="date", lookup_expr="gte", label="Published Date From"
    )

	category = filters.CharFilter(
        field_name="category",
        lookup_expr="icontains",
        label="Category Contains",
    )
	
	description = filters.CharFilter(
        field_name="description",
        lookup_expr="icontains",
        label="Description Contains",
    )

	class Meta:
		model = Publication
		fields = [
			"title", 
			"category", "description", "date"
			]