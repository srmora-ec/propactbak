from django.urls import path
from .views import (
    MyTokenObtainPairView,
    ClausulaCreateView,
    ClausulaUpdateView,
    ClausulaDeleteView,
    ContratoCreateView,
    ContratoUpdateView,
    TokenValidationView,
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/clausula/create/', ClausulaCreateView.as_view(), name='clausula_create'),
    path('api/clausula/update/<int:pk>/', ClausulaUpdateView.as_view(), name='clausula_update'),
    path('api/clausula/delete/<int:pk>/', ClausulaDeleteView.as_view(), name='clausula_delete'),
    path('api/contrato/create/', ContratoCreateView.as_view(), name='contrato_create'),
    path('api/contrato/update/<int:pk>/', ContratoUpdateView.as_view(), name='contrato_update'),
    path('api/token/validate/', TokenValidationView.as_view(), name='token_validate'),

]
