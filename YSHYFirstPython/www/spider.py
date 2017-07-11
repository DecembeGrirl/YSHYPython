
#简单爬虫 获取网页中的 .jpg 图片

#coding=utf-8
import urllib
import urllib.request
import re
import ssl


def getHtml(url):
    # 全局取消 ssl 验证
    ssl._create_default_https_context = ssl._create_unverified_context
    page = urllib.request.urlopen(url)
    #html = page.read()  # 读取URL上的数据
    html = page.read() #读取URL上的数据
    return html

def getBaiduImageHtml(url):
    # 全局取消 ssl 验证
    ssl._create_default_https_context = ssl._create_unverified_context
    User_Agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Mobile Safari/537.36'
    Accept_Encoding = 'gzip, deflate'
    Accept = 'image/webp,image/apng,image/*,*/*;q=0.8'
    Host = 'imgstat.baidu.com'
    Proxy_Connection = 'keep - alive'
    headers = {'User-Agent': User_Agent, 'Accept-Encoding': Accept_Encoding, 'Accept': Accept, 'Host': Host, 'Proxy-Connection': Proxy_Connection}
    request = urllib.request.Request(url, headers) #将header 请求头和 URL封装为一个
    page = urllib.request.urlopen(request)
    html = page.read()
    return html

def getImg(html):
    # print(html)
    # reg = r'src="(.+?\.jpg)" pic_ext'  #  获取.jpg 图片的正则表达式
    reg = r'src="(.+?\.jpg)"'
    # reg = r'src="(.+?\.gif)"'
    # reg = r'src="^http(.*)\.jpg$"'
    imgre = re.compile(reg)   # 把正则表达式编译成一个正则表达式对象
    html = html.decode('utf-8') # python3 需要将 html 进行utf-8编码
    imglist = re.findall(imgre, html)   # 读取html 中包含 imgre（正则表达式）的数据
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, './resource/%s.jpg' % x)  # 直接将远程数据下载到本地。第二个参数为存放的具体路径, 如果没有写路径则默认为当前文件夹下
        x += 1
    return imglist
# html = getHtml('http://tieba.baidu.com/p/2460150866')
html = getHtml('http://www.sj33.cn/dphoto/stsy/200908/20652_4.html')
# html = getBaiduImageHtml('https://image.baidu.com/')
print(getImg(html))














