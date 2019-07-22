 #定义代码格式
#-*- coding:utf8 -*-
from urllib import request
from urllib import parse
from urllib.request import urlopen
url = "http://reg.haibian.com/login/ajax_login"
#定义请求数据并赋值
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '111111'#密码应该是MD5的，在百度翻译，这里不知道为什么明文就可以通过
data = parse.urlencode(data)
#将数据和url进行连接
requests = url+'?'+data
#打开请求获取对象
requestResponse = urlopen(requests)
#读取服务端返回的对象
responseStr = requestResponse.read()
#打印数据
#ResponseStr = responseStr.decode("unicode_escape")   #将密码进行转译（因为密码用的是MD5的，对应上边）
print(responseStr)