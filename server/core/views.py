from rest_framework import viewsets
from core.models import Menu
from core.serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.all()