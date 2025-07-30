from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.transactions.models.directory import Status, Type, Category, SubCategory
from apps.transactions.serializers import StatusSerializer, TypeSerializer, CategorySerializer, SubCategorySerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


@api_view(['GET'])
@permission_classes([IsAdminUser])
def categories_by_type(request):
    type_id = request.query_params.get('type_id')
    if not type_id:
        return Response({"error": "type_id parameter is required"}, status=400)
    categories = Category.objects.filter(type_id=type_id)
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def subcategories_by_category(request):
    category_id = request.query_params.get('category_id')
    if not category_id:
        return Response({"error": "category_id parameter is required"}, status=400)
    subcategories = SubCategory.objects.filter(category_id=category_id)
    serializer = SubCategorySerializer(subcategories, many=True)
    return Response(serializer.data)
