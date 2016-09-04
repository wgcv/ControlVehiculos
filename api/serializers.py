from .models import Emergencia, Unidad
from rest_framework import serializers


class EmergenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emergencia
        fields = ('id','alarma', 'direccion', 'latitud', 'longitud')


class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unidad
        fields = ('id','nombre', 'tipo', 'latitud','longitud')