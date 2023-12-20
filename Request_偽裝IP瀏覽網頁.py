import requests, random

# 查詢自己電腦的IP
ip= requests.get("https://api.ipify.org/")

# 代理伺服器 https://free-proxy-list.net/

proxy ip=["220.73.173.111","47.56.110.204"]
#隨機抽選一個代理ip,也可以寫一個爬蟲來爬蟲Ip
ip= random.choice(proxy.ip)
print("使用proxy的Ip:%s"%ip)

#使用代理ip去連pchome網站
proxie={"http://"ip,"http://"ip}
web= requests.get
