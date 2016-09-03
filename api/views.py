from django.shortcuts import render
from .models import Emergencia, Unidad
from rest_framework import viewsets
from .serializers import EmergenciaSerializer, UnidadSerializer


class EmergenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Emergencia.objects.all()
    serializer_class = EmergenciaSerializer


class UnidadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer