from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from faculty_website_backend.users.api.views import UserViewSet
from faculty_website_backend.publications.api.views import PublicationViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# router.register("users", UserViewSet)
router.register("publications", PublicationViewSet)



app_name = "api"
urlpatterns = router.urls
