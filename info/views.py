import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Info
from .serializers import InfoSerializer


# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")


@api_view(['GET'])
def helloAPI(request, id):
    totalInfos = Info.objects.all()
    randomInfos = random.sample(list(totalInfos), id)
    serializer = InfoSerializer(randomInfos, many=True)
    return Response(serializer.data)


