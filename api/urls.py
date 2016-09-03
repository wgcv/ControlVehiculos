from django.conf.urls import url, include
from django.contrib.auth.models import Emergencia
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class EmergenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emergencia
        fields = ('alarma', 'direccion', 'latitud', 'longitud')

# ViewSets define the view behavior.
class EmergenciaViewSet(viewsets.ModelViewSet):
    queryset = Emergencia.objects.all()
    serializer_class = EmergenciaSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]