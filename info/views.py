import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Info
from .serializers import InfoSerializer
from .news_crawler import collect_news


@api_view(['GET'])
def getSubscriptions(request, startDate, endDate, isNearyBy):
    return Response()


@api_view(['GET'])
def getSubscriptionDeatil(request, id):
    return Response()


@api_view(['GET'])
def getCurations(request, curation):
    return Response()


@api_view(['GET'])
def getRecentlies(request):
    totalInfos = Info.objects.all()
    randomInfos = random.sample(list(totalInfos), id)
    serializer = InfoSerializer(randomInfos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def postNews(request):
    news = collect_news()
    return Response(news)


