from _datetime import datetime

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .news_crawler import collect_news
from .subscription_api import *

from drf_yasg.utils import swagger_auto_schema
from api.serializers import NearbySerializer


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
                'type_kor': '아파트',
                'type_eng': 'apt',
            }
            apt_list.append(apt_one)
        for urbty in urbties:
            urbty_one = {
                'manage_no': urbty.HOUSE_MANAGE_NO,
                'title': urbty.BSNS_MBY_NM,
                'location': urbty.HSSPLY_ADRES,
                'rcept_bgnde': urbty.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': urbty.SUBSCRPT_RCEPT_ENDDE,
                'type_kor': '오피스텔/도시형/민간임대',
                'type_eng': 'urbty',
            }
            apt_list.append(urbty_one)
        for remndr in remndres:
            remndr_one = {
                'manage_no': remndr.HOUSE_MANAGE_NO,
                'title': remndr.BSNS_MBY_NM,
                'location': remndr.HSSPLY_ADRES,
                'rcept_bgnde': remndr.SUBSCRPT_RCEPT_BGNDE,
                'rcept_endde': remndr.SUBSCRPT_RCEPT_ENDDE,
                'type_kor': '무순위/잔여세대',
                'type_eng': 'remndr',
            }
            apt_list.append(remndr_one)

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


@api_view(['GET'])
def getDetail(request, id):
    subject = request.GET.get('subject', 'apt')

    detail_value_list = []
    if subject == 'remndr':
        remndr = Remndr.objects.get(HOUSE_MANAGE_NO=id)
        details = RemndrDetail.objects.filter(HOUSE_MANAGE_NO=id)
        for val in details:
            input_value = {}
            input_value['SPSPLY_HSHLDCO'] = val.SUPLY_HSHLDCO
            input_value['SUPLY_AR'] = val.SUPLY_AR
            input_value['LTTOT_TOP_AMOUNT'] = val.LTTOT_TOP_AMOUNT
            input_value['CNSTRCT_ENTRPS_NM'] = remndr.BSNS_MBY_NM
            detail_value_list.append(input_value)

    elif subject == 'urbty':
        urbty = Urbty.objects.get(HOUSE_MANAGE_NO=id)
        details = UrbtyDetail.objects.filter(HOUSE_MANAGE_NO=id)
        for val in details:
            input_value = {}
            input_value['SPSPLY_HSHLDCO'] = val.SUPLY_HSHLDCO
            input_value['SUPLY_AR'] = val.SUPLY_AR
            input_value['LTTOT_TOP_AMOUNT'] = val.SUPLY_AMOUNT
            input_value['CNSTRCT_ENTRPS_NM'] = urbty.BSNS_MBY_NM
            detail_value_list.append(input_value)
    else:
        apt = Apt.objects.get(HOUSE_MANAGE_NO=id)
        apt_details = AptDetail.objects.filter(HOUSE_MANAGE_NO=id)
        for val in apt_details:
            input_value = {}
            input_value['SPSPLY_HSHLDCO'] = val.SPSPLY_HSHLDCO
            input_value['SUPLY_AR'] = val.SUPLY_AR
            input_value['LTTOT_TOP_AMOUNT'] = val.LTTOT_TOP_AMOUNT
            input_value['CNSTRCT_ENTRPS_NM'] = apt.CNSTRCT_ENTRPS_NM
            detail_value_list.append(input_value)

    return JsonResponse({
        'value': detail_value_list,
        'timestamp': datetime.today()
    })


@api_view(['GET'])
@swagger_auto_schema(query_serializer=NearbySerializer)
def nearby(request):
    # 현재위치 기반 찾기
    x = request.GET.get('x', '126.8136053')
    y = request.GET.get('y', '37.5651639')
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=" + x + "&y=" + y
    headers = {"Authorization": "KakaoAK afdb43b5fe201bb1deab2af24e440efa"}
    api_test = requests.get(url, headers=headers)
    region = api_test.json()['documents'][0]['region_1depth_name'] + " " + api_test.json()['documents'][0]['region_2depth_name']
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
            'type_kor': '아파트',
            'type_eng': 'apt',
        }
        apt_list.append(apt_one)
    for urbty in urbties:
        urbty_one = {
            'manage_no': urbty.HOUSE_MANAGE_NO,
            'title': urbty.BSNS_MBY_NM,
            'location': urbty.HSSPLY_ADRES,
            'rcept_bgnde': urbty.SUBSCRPT_RCEPT_BGNDE,
            'rcept_endde': urbty.SUBSCRPT_RCEPT_ENDDE,
            'type_kor': '오피스텔/도시형/민간임대',
            'type_eng': 'urbty',
        }
        apt_list.append(urbty_one)
    for remndr in remndres:
        remndr_one = {
            'manage_no': remndr.HOUSE_MANAGE_NO,
            'title': remndr.BSNS_MBY_NM,
            'location': remndr.HSSPLY_ADRES,
            'rcept_bgnde': remndr.SUBSCRPT_RCEPT_BGNDE,
            'rcept_endde': remndr.SUBSCRPT_RCEPT_ENDDE,
            'type_kor': '무순위/잔여세대',
            'type_eng': 'remndr',
        }
        apt_list.append(remndr_one)

    return JsonResponse({
        'value': sorted(apt_list, key=lambda i: i['rcept_bgnde'], reverse=True),
        'timestamp': datetime.today()
    })


class News(APIView):
    def get(self, request):
        news = collect_news()
        return Response(news)
