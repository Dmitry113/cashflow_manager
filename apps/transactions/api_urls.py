from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.admin_views import category_by_type, subcategory_by_category
from .views.transaction_views import TransactionViewSet
from .views.directory_views import StatusViewSet, TypeViewSet, CategoryViewSet, SubCategoryViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'statuses', StatusViewSet, basename='status')
router.register(r'types', TypeViewSet, basename='type')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'subcategories', SubCategoryViewSet, basename='subcategory')

urlpatterns = [
    path('', include(router.urls)),  # Автоматически подставляет маршруты DRF
    path('category_by_type/', category_by_type, name='category_by_type'),
    path('subcategory_by_category/', subcategory_by_category, name='subcategory_by_category'),
]
