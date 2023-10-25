from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Users, Houses
from .serializers import HousesListSerializer, HousesDetailSerializer
from rest_framework import viewsets
class ListUsers(APIView):
    def get(self, request, format=None):
        logins = [user.login for user in Users.objects.all()]
        return Response(logins)


class HousesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Houses.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return HousesListSerializer
        elif self.action == "retrieve":
            return HousesDetailSerializer