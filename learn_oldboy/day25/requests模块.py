import requests

response=requests.get("https://www.baidu.com/s",
                      params={"wd": "美女","a": 1},
                      headers={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
                      })

print(response.status_code)
print(response.text)
print(response.json())


# requests.post("",data={})



with open("jd.html","w",encoding = "utf8") as f:
    f.write(response.text)