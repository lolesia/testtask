from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home')
]