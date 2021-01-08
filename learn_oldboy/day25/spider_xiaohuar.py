
import requests
import re
import hashlib

res=requests.get("http://www.xiaohuar.com/list-3-0.html")

url_list=re.findall('<div class="items">.*?href="(.*?)"',res.text,re.S)
print(url_list)
count=1
for url in url_list:
    
    res=requests.get(url)
    # print("res---->",res.text)
    ret=re.search('<video.*?source src="(?P<path>.*?)"',res.text,re.S)
    print(ret.group("path"))

    detail_url=ret.group("path")
    res=requests.get(detail_url)

    print("detail_url",detail_url)

    with open("%s.mp4"%count,"wb") as f:
        f.write(res.content)

    count+=1
