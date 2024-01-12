from rest_framework.routers import SimpleRouter
from apps.item.api import views

"""
Item Routers
"""

app_name = "item_urls"
item_router = SimpleRouter()

item_router.register(r'items/price', views.ItemPriceSumViewSet, basename='item-price')
item_router.register(r'items', views.ItemViewSet, basename='item')

urlpatterns = item_router.urls
