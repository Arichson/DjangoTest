from .models import Dum
from django.contrib.auth.models import User, Group
from rest_framework import serializers
# Our DumSerializer
class DumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Dum
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'details']