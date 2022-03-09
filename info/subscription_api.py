import requests

from .models import *

api_key = "tUJXMx507TgYQn2vJOL0q+WiOMNLBuJKtPRH/JPmgKdyOUtg4OZBAAlS8QKzDmLyMkhmIj9b6K0bKNULwIL0Dg=="
api_key_dcode = requests.utils.unquote(api_key, encoding='utf-8')
url = "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1"
parameters = {
    'serviceKey': api_key,
    'perPage': 10000,
    # 'startmonth': '202101', 'endmonth': '202103', 'houseSecd': '01', 'sido': '강원',
    # 'houseName': '횡성 벨라시티', 'rentSecd': '0'
}


def getApt():
    req = requests.get(url + '/getAPTLttotPblancDetail', params=parameters)
    return req


def getAptDetail():
    req = requests.get(url + '/getAPTLttotPblancMdl', params=parameters)
    return req


def getUrbyty():
    req = requests.get(url + '/getUrbtyOfctlLttotPblancDetail', params=parameters)
    return req


def getUrbytyDetail():
    req = requests.get(url + '/getUrbtyOfctlLttotPblancMdl', params=parameters)
    return req


def getRemndr():
    req = requests.get(url + '/getRemndrLttotPblancDetail', params=parameters)
    return req


def getRemndrDetail():
    req = requests.get(url + '/getRemndrLttotPblancMdl', params=parameters)
    return req


def saveApt(apts):
    json_data = apts.json()['data']

    for val in json_data:
        apt = Apt().from_json(val)
        apt.save()


def saveUrbty(urbty):
    json_data = urbty.json()['data']

    for val in json_data:
        urbtyVal = Urbty().from_json(val)
        urbtyVal.save()


def saveRemndr(remndr):
    json_data = remndr.json()['data']

    for val in json_data:
        apt_detail = Urbty(val)
        apt_detail.save()


