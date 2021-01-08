import csv
import json


#
# file_name = './data.csv'
# with open(file_name) as f:
#     data = csv.reader(f)
#     print list(data)

json.loads(str)   #json--字典  有序--无序  反序列化
json.dumps(dict)  #字典--json  无序--有序  序列化


data = {
        "business_autoFans_J": [{"2016_08": 14}, {"2016_09": 15}, {"2016_10": 9}],
        "autoAX": [{"2016_08": 7}, {"2016_09": 32}, {"2016_10": 0}],
        "autoAX_admin": [{"2016_08": 5}, {"2016_09": 13}, {"2016_10": 2}],
    }