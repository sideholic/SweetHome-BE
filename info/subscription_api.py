import requests

api_key = "OJZ9FrlEdT7%252BvgBrdLN4C%252FOeYhGVPV0t6VaSIUuZX6T7AqeBTFHcuyKiVf1nOD3n9FNRtbhCgBesvmVUFNdSwg%253D%253D"
api_key_dcode = requests.utils.unquote(api_key, encoding='utf-8')


def get_lttot_pblanc_list():
    parameters = {'ServiceKey': 'tUJXMx507TgYQn2vJOL0q%252BWiOMNLBuJKtPRH%252FJPmgKdyOUtg4OZBAAlS8QKzDmLyMkhmIj9b6K0bKNULwIL0Dg%253D%253D',
                  'startmonth': '202101', 'endmonth': '202103', 'houseSecd': '01', 'sido': '강원',
                  'houseName': '횡성 벨라시티', 'rentSecd': '0'}

    print(parameters)

    url = "http://openapi.reb.or.kr/OpenAPI_ToolInstallPackage/service/rest/ApplyhomeInfoSvc/getLttotPblancList"
    req = requests.get(url, params=parameters)
    return req
