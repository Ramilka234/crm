from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Users

class ListUsers(APIView):
    def get(self, request, format=None):
        logins = [user.login for user in Users.objects.all()]
        return Response(logins)
