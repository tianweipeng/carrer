import requests
from lxml import html


# 注册
def rejister(account, password):
    # 西交注册上传时，有一个refid，需先获取此id
    url_re = "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so"
    header_re = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/zpfw.so",
        "host": "jiuye.swjtu.edu.cn"
    }

    param = {"type": "dwzc"}
    response = requests.get(url_re, headers=header_re, params=param)
    etree = html.etree
    content = etree.HTML(response.text)
    refid = content.xpath("/html/body/div[4]/div/div/form/input[2]/@value")[0]

    # 上传
    url_up = "http://jiuye.swjtu.edu.cn/eweb/servlet/resuploadnew"
    header_up = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc"
    }

    with open('C:\\Users\\dell\\Desktop\\pkq2.jpg', 'rb') as f:
        pass

    files = {'refid':(None, refid),'reftype':(None,'zzjgdmzsmj'),'mdbFiles':('2019.png',f,'image/jpg')}
    reponse = requests.post(url_up,headers=header_up,files=files)

    # print(requests.Request('POST', url_up, headers=header, files=files).prepare().body.decode('ascii'))
    # text = reponse.text
    # print (text)

    # 注册


if __name__ == '__main__':
    rejister("a","aa")