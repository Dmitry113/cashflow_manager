from django.http import JsonResponse
from apps.transactions.models.directory import Category, SubCategory
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_GET


@staff_member_required
@require_GET
def category_by_type(request):
    type_id = request.GET.get('type_id')  # ← исправлено
    categories = Category.objects.filter(type_id=type_id).order_by('name') if type_id else []
    data = [{'id': c.id, 'name': c.name} for c in categories]
    return JsonResponse(data, safe=False)


@staff_member_required
@require_GET
def subcategory_by_category(request):
    category_id = request.GET.get('category_id')  # ← исправлено
    subcategories = SubCategory.objects.filter(category_id=category_id).order_by('name') if category_id else []
    data = [{'id': sc.id, 'name': sc.name} for sc in subcategories]
    return JsonResponse(data, safe=False)
