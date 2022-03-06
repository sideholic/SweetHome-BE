from rest_framework.response import Response
from rest_framework.views import APIView

from .news_crawler import collect_news
from .subscription_api import get_lttot_pblanc_list


class Subscription(APIView):
    def get(self, request):
        lttot_pblanc_list = get_lttot_pblanc_list()
        return Response(lttot_pblanc_list)

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


