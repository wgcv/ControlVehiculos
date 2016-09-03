from .models import Emergencia, Unidad
from rest_framework import serializers


class EmergenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emergencia
        fields = ('alarma', 'direccion', 'latitud', 'longitud')


class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ('nombre', 'tipo', 'latitud','longitud')