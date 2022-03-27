from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import Userprofile

@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)