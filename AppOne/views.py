from django.contrib.auth.models import User
from rest_framework import viewsets


# def index(request):
#     return HttpResponse('123')
from AppOne.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = GroupSerializer
