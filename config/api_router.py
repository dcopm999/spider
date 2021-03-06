from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from spider.products.views import CategoryViewSet, CompanyViewSet, ProductViewSet
from spider.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("categories", CategoryViewSet)
router.register("companies", CompanyViewSet)
router.register("products", ProductViewSet)

app_name = "api"

urlpatterns = router.urls
