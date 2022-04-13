#coding:utf-8
import requests

'''
get
params = ‘字典’  把字典的key=value   url?

post
url-encode
data = ‘字典’ 把字典的key=value  post正文里

xml json 
data = ‘字符串’ post正文

json 
json = ‘字典’   拼成json字符串 post正文里
'''
# get
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
# # url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3117'
# para = {'theRegionCode': '3117'}
# print requests.get(url=url,params=para).text
# # print type(requests.get(url=url,params=para).text)

#post
# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
# head = {'Content-Type': 'application/x-www-form-urlencoded'}
# data = {'theRegionCode': '3117'}
# response = requests.post(url=url, headers=head, data=data)
# print response.text

# url = 'http://139.199.132.220:8000/event/weather/getWeather/'
# headers = {'Content-Type': 'application/json'}
# paras = {'theCityCode': 1}
# response = requests.post(url=url, headers=headers, json=paras)
# print response.text
# # print response.json()['date']

# url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
# head = {'Content-Type': 'text/xml'}
# data = '''<?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <getSupportCityString xmlns="http://WebXml.com.cn/">
#       <theRegionCode>3117</theRegionCode>
#     </getSupportCityString>
#   </soap:Body>
# </soap:Envelope>'''
# response = requests.post(url=url, headers=head, data=data)
# print response.text