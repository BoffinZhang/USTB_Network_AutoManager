# USTB School Network AutoLogin

# ------ import packages
import requests
import socket      # 获取本机ip。若要连接ipv6，POST请求中必须要有v6的地址      
# ------ url of login page
url = 'http://202.204.48.82'

# ------ user accout&password
username = "41724081"
password = "235711zhang"

# ------ get ip
# myIP[2][4][0]就是咱们的ipv6地址了
myIP = socket.getaddrinfo(socket.gethostname(),None)
v6addr = myIP[2][4][0]

# form post request
# TODO use .json to rewrite this part
mydata = 'DDDDD='+username+'&upass='+password+'&savePWD='+'&v6ip='+v6addr+'&0MKKey=123456789'
z=requests.post(url,data=mydata)


# Tips

# 1. 如果你发现脚本不能用，可以打印返回的IP地址表，查看自己的IP信息
# print(myIP[2][4][0])
# for item in myIP:
#     print(item)