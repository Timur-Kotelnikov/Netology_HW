from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, StockViewSet, PersonViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)
router.register('persons', PersonViewSet)

urlpatterns = router.urls
