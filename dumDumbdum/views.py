from .models import Dum
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DumSerializer
class DumViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Dum.objects.all()
    # The serializer class for serializing output
    serializer_class = DumSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]