# USTB_Network_AutoManager
北京科技大学校园网登录脚本（更新中）——python练手项目
其实代码非常简单，最主要的就是发送一条post请求

## 关于POST请求
在登录校园网的时候，我用Fiddler抓取到了这样一条网络请求：
```
DDDDD=41******&upass=******&savePWD=&v6ip=2001%3A0da8%3A0208%*****%******%*****%3A4a59%3A3bb4&0MKKey=123456789
```
这条请求里用明码写出了用户名和密码，还有V6的ip地址，于是我们直接在脚本中生成字符串，传递参数即可

## 关于IPV6地址
我试了一下，如果请求中v6ip参数为空，登录之后是没有ipv6连接的，因此我们必须得传递v6的地址给它。
具体可以用python的socket包，下面的代码可以打印出本机的所有ip信息
```python
for item in myIP:
    print(item)
```
在我这里，myIP[2][4][0]就是我的的ipv6地址，如果在使用脚本的过程，总是无法连接v6，不妨试试是不是这里有问题。

## github链接
github上会有最新的项目：
https://github.com/BoffinZhang/USTB_Network_AutoManager
