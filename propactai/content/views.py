from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Clausula, Contrato
from .serializers import ClausulaSerializer, ContratoSerializer

# Vista para generar el token de acceso
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    # Esta clase puede personalizarse si se necesita un comportamiento adicional
    pass


# Vista para crear una clausula
class ClausulaCreateView(generics.CreateAPIView):
    queryset = Clausula.objects.all()
    serializer_class = ClausulaSerializer
    permission_classes = [IsAuthenticated]


# Vista para editar una clausula
class ClausulaUpdateView(generics.UpdateAPIView):
    queryset = Clausula.objects.all()
    serializer_class = ClausulaSerializer
    permission_classes = [IsAuthenticated]


# Vista para eliminar una clausula
class ClausulaDeleteView(generics.DestroyAPIView):
    queryset = Clausula.objects.all()
    permission_classes = [IsAuthenticated]


# Vista para crear un contrato
class ContratoCreateView(generics.CreateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]


# Vista para editar un contrato
class ContratoUpdateView(generics.UpdateAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated]

# Vista para listar las cláusulas
class ClausulaListView(generics.ListAPIView):
    queryset = Clausula.objects.all()
    serializer_class = ClausulaSerializer

# Vista para listar los contratos
class ContratoListView(generics.ListAPIView):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer


# Vista para verificar si el token es válido
class TokenValidationView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.check_blacklist()
            return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)
