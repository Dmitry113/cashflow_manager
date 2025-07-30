from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API маршруты
    path('api/', include('apps.transactions.api_urls')),

    # HTML-шаблоны (frontend)
    path('transactions/', include('apps.transactions.urls')),

    # Главная страница
    path('', TemplateView.as_view(template_name="transactions/home.html"), name='home'),
]
