import requests

from .models import Info, Apt

api_key = "tUJXMx507TgYQn2vJOL0q+WiOMNLBuJKtPRH/JPmgKdyOUtg4OZBAAlS8QKzDmLyMkhmIj9b6K0bKNULwIL0Dg=="
api_key_dcode = requests.utils.unquote(api_key, encoding='utf-8')
url = "https://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1"


def getApt():
    parameters = {
        'serviceKey': api_key,
        'perPage': 10000,
        # 'startmonth': '202101', 'endmonth': '202103', 'houseSecd': '01', 'sido': '강원',
        # 'houseName': '횡성 벨라시티', 'rentSecd': '0'
    }
    req = requests.get(url + '/getAPTLttotPblancDetail', params=parameters)
    return req


def saveApt(apts):
    json_data = apts.json()['data']

    for val in json_data:
        apt = Apt().from_json(val)
        apt.save()


