from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from quickstart.serializers import GroupSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """_summary_
    
    Endpoint da API que permite que os usuários sejam visualizados ou editados.

    Args:
        viewsets (_type_): _description_
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API que permite que grupos sejam visualizados ou editados.
    """
    
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
