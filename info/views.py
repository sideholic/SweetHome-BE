import json

from rest_framework.response import Response
from rest_framework.views import APIView

from .news_crawler import collect_news
from .subscription_api import *


class Subscription(APIView):
    def get(self, request):
        lttot_pblanc_list = getApt()
        save_urbty_list = getUrbyty()
        saveApt(lttot_pblanc_list)
        saveUrbty(save_urbty_list)
        return Response("complete")

    def post(self, request, id):
        return Response()

    # def getCurations(request, curation):
    #     return Response()

    # def getRecentlies(request):
    #     totalInfos = Info.objects.all()
    #     randomInfos = random.sample(list(totalInfos), id)
    #     serializer = InfoSerializer(randomInfos, many=True)
    #     return Response(serializer.data)


class News(APIView):
    def get(self, request):
        news = collect_news()
        return Response(news)


