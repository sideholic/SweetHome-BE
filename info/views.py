from _datetime import datetime, timedelta

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .news_crawler import collect_news
from .subscription_api import *
import json

class Nearby(APIView):
    def get(self, request):
        # 현재위치 기반 찾기
        url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=127.1086228&y=37.4012191"
        headers = {"Authorization": "KakaoAK afdb43b5fe201bb1deab2af24e440efa"}
        api_test = requests.get(url, headers=headers)
        region = api_test.json()['documents'][0]['region_1depth_name']
        apts = Apt.objects.filter(HSSPLY_ADRES__contains=region)
        urbties = Urbty.objects.filter(HSSPLY_ADRES__contains=region)
        remndres = Remndr.objects.filter(HSSPLY_ADRES__contains=region)

        apt_list = []
        for apt in apts:
            apt_one = {
                'manage_no': apt.HOUSE_MANAGE_NO,
                'title': apt.BSNS_MBY_NM,
                'location': apt.HSSPLY_ADRES,
                'rcept_bgnde': apt.RCEPT_BGNDE,
                'rcept_endde': apt.RCEPT_ENDDE,
                'type': '아파트',
            }
            apt_list.append(apt_one)

        urbty_list = []
        for urbty in urbties:
            urbty_one = {
                'manage_no': urbty.HOUSE_MANAGE_NO,
                'title': urbty.BSNS_MBY_NM,
                'location': urbty.HSSPLY_ADRES,
                'rcept_bgnde': urbty.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': urbty.SUBSCRPT_RCEPT_ENDDE,
                'type': '오피스텔/도시형/민간임대',
            }
            apt_list.append(urbty_one)

        remndr_list = []
        for remndr in remndres:
            remndr_one = {
                'manage_no': remndr.HOUSE_MANAGE_NO,
                'title': remndr.BSNS_MBY_NM,
                'location': remndr.HSSPLY_ADRES,
                'rcept_bgnde': remndr.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': remndr.SUBSCRPT_RCEPT_ENDDE,
                'type': '무순위/잔여세대',
            }
            apt_list.append(remndr_one)

        return JsonResponse({
            'value': sorted(apt_list, key=lambda i: i['rcept_bgnde'], reverse=False),
            'timestamp': datetime.today()
        })


class Subscription(APIView):
    def get(self, request):
        now_string = datetime.today().strftime('%Y-%m-%d')
        # now_string = datetime.today() - timedelta(days=7)

        apts = Apt.objects.filter(RCEPT_BGNDE__gt=now_string)
        urbties = Urbty.objects.filter(SUBSCRPT_RCEPT_BGNDE__gt=now_string)
        remndres = Remndr.objects.filter(SUBSCRPT_RCEPT_BGNDE__gt=now_string)

        apt_list = []
        for apt in apts:
            apt_one = {
                'manage_no': apt.HOUSE_MANAGE_NO,
                'title': apt.BSNS_MBY_NM,
                'location': apt.HSSPLY_ADRES,
                'rcept_bgnde': apt.RCEPT_BGNDE,
                'rcept_endde': apt.RCEPT_ENDDE,
                'type': '아파트',
            }
            apt_list.append(apt_one)

        urbty_list = []
        for urbty in urbties:
            urbty_one = {
                'manage_no': urbty.HOUSE_MANAGE_NO,
                'title': urbty.BSNS_MBY_NM,
                'location': urbty.HSSPLY_ADRES,
                'rcept_bgnde': urbty.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': urbty.SUBSCRPT_RCEPT_ENDDE,
                'type': '오피스텔/도시형/민간임대',
            }
            apt_list.append(urbty_one)

        remndr_list = []
        for remndr in remndres:
            remndr_one = {
                'manage_no': remndr.HOUSE_MANAGE_NO,
                'title': remndr.BSNS_MBY_NM,
                'location': remndr.HSSPLY_ADRES,
                'rcept_bgnde': remndr.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': remndr.SUBSCRPT_RCEPT_ENDDE,
                'type': '무순위/잔여세대',
            }
            apt_list.append(remndr_one)

        # apt_list = json.loads(serializers.serialize('json', apts))
        # urbty_json_list = json.loads(serializers.serialize('json', urbty))
        # remndr_json_list = json.loads(serializers.serialize('json', remndr))

        return JsonResponse({
            'value': sorted(apt_list, key=lambda i: i['rcept_bgnde'], reverse=False),
            'timestamp': datetime.today()
        })


    def post(self, request):
        lttot_pblanc_list = getApt()
        save_urbty_list = getUrbyty()
        save_remndr_list = getRemndr()
        save_apt_detail = getAptDetail()
        save_urbyty_detail = getUrbytyDetail()
        save_remndr_detail = getRemndrDetail()
        saveApt(lttot_pblanc_list)
        saveUrbty(save_urbty_list)
        saveRemndr(save_remndr_list)
        saveAptDetail(save_apt_detail)
        saveUrbtyDetail(save_urbyty_detail)
        saveRemndrDetail(save_remndr_detail)
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


