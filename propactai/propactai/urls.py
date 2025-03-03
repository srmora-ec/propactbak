"""
URL configuration for propactai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from content.views import (
    MyTokenObtainPairView,
    ClausulaCreateView,
    ClausulaUpdateView,
    ClausulaDeleteView,
    ContratoCreateView,
    ContratoUpdateView,
    TokenValidationView,
    ClausulaListView,
    ContratoListView,
    RefreshToken
)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/clausula/create/', ClausulaCreateView.as_view(), name='clausula_create'),
    path('api/clausula/update/<int:pk>/', ClausulaUpdateView.as_view(), name='clausula_update'),
    path('api/clausula/delete/<int:pk>/', ClausulaDeleteView.as_view(), name='clausula_delete'),
    path('api/contrato/create/', ContratoCreateView.as_view(), name='contrato_create'),
    path('api/contrato/update/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('api/token/validate/', TokenValidationView.as_view(), name='token_validate'),
    path('api/clausula/clausulas/', ClausulaListView.as_view(), name='clausula-list'),
    path('api/contrato/contratos/', ContratoListView.as_view(), name='contrato-list'),
    path('api/token/refresh/', RefreshToken, name='token_refresh'),  
]