from config import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from apps.item.api import urls as item_urls
from apps.auth import urls as admin_urls
from apps.utils import urls as health_url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(health_url, namespace="health-url")),
    path("api/v1/", include(item_urls, namespace="api-urls")),
    path("api/v1/", include(admin_urls, namespace="admin-urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
