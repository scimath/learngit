#coding:utf-8
import urllib
import urllib2
import cookielib
import re

print '-------------xzp西南交大成绩查询系统-v1.0---------'
userid = raw_input("请输入学号：")
password = raw_input("请输入密码：")
print "--------------------------------------------------"
#hosturl = "http://202.115.67.2/service/login.jsp?user_type=student"
#获取一个保存cookie的对象
cj = cookielib.LWPCookieJar()
#将一个保存cookie对象，和一个HTTP的cookie的处理器绑定
cookie_support = urllib2.HTTPCookieProcessor(cj)
#创建一个opener，将保存了cookie的http处理器，还有设置一个handler用于处理http的URL的打开
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
#将包含了cookie、http处理器、http的handler的资源和urllib2对象板顶在一起
urllib2.install_opener(opener)

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

headers2 = {
				#"Cookie":"JSESSIONID=D6E112103A00681FD31D8758A254CCD0.worker2; user_id=20110097; user_type=student; user_style=modern",
				"Host":"202.115.67.2",
				"Referer":"http://202.115.67.2/servlet/UserLoginSQLAction",
				"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36"
}

url2 = "http://202.115.67.2/usersys/index.jsp"
req2 = urllib2.Request(url2)
for n in headers2:
	req2.add_header(n,headers2[n])

html2 = urllib2.urlopen(req2).read()

url3 = "http://202.115.67.2/servlet/CheckStudentSubmitAppraiseAction"

headers3 = {
				"Host":"202.115.67.2",
				"Referer":"http://202.115.67.2/usersys/index.jsp",
				"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36"
}
req3 = urllib2.Request(url3)

for n in headers3:
	req.add_header(n,headers3[n])

html3 = urllib2.urlopen(req3).read()

url4 = "http://202.115.67.2/student/score/ScoreNew.jsp?SelectType=ALL"
req4 = urllib2.Request(url4)
headers4 = {
				"Host":"202.115.67.2",
				"Referer":"http://202.115.67.2/student/score/ScoreNew.jsp",
				"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36"
}

for n in headers4:
	req4.add_header(n,headers4[n])

html4 = urllib2.urlopen(req4).read()

url5 = "http://202.115.67.2/student/course/MyCourseThisTerm.jsp"

headers5 = {
				"Host":"202.115.67.2",
  				"Referer":"http://202.115.67.2/usersys/index.jsp",
				"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36"
}
req5 = urllib2.Request(url5)

for n in headers5:
	req5.add_header(n,headers5[n])

html5 = urllib2.urlopen(req5).read()

classname = re.findall("\S+(?=<\/td>\s+<td\sheight=\"26\"\swidth=\"6%\"\salign=\"center\">)",html4)
score = re.findall("(?<=style=font-size:13px;>).+(?=<\/font>)",html4)
course = re.findall("\S+(?=\s+<\/td>\s)",html5)
time = re.findall("(?<=<td\sheight=\"28\"\swidth=\"20%\"\salign=\"center\"\sstyle=\"line-height:\s150%\">).+(?=<br>)",html5)
if len(classname)!= 0 :
	print "用户名或者密码错误！"
else:
	print userid+'您的成绩为:'
	for n in range(len(classname)):
		print "%d." %(n+1)
		print classname[n].decode('utf-8')
		print score[n].decode('utf-8')
		print "--------------------"
	print "您的课表为："
	print "-----------------------------------"
	for m in range(len(time)):
		print course[m]
		print time[m]
		print "--------------------"
	print html4



