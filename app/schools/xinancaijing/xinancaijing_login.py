# -*- coding: utf-8 -*-
import time
from PIL import Image
import requests
from app.schools.xinancaijing import xinancaijing_js_analyse


# 登陆方法
def login(account, password):
    # 获取cookie
    url = "https://jobzpgl.swufe.edu.cn/job/login/index.html"
    response = requests.get(url)
    cookies = response.cookies.get_dict()
    print(cookies)

    # 利用cookie重置验证码（暂时没有自动识别验证码图片程序）
    url2 = "https://jobzpgl.swufe.edu.cn/Job/Login/verify.html"
    response2 = requests.get(url2, cookies=cookies)
    with open("C:\\Users\\dell\\Desktop\\test.jpg", 'wb') as f:
        f.write(response2.content)
        f.close()
    time.sleep(3)
    im = Image.open('C:\\Users\\dell\\Desktop\\test.jpg')
    im.show()

    code = input("input:")

    formdata = {
        "account": account,
        "password": xinancaijing_js_analyse.get_password(password),
        "verify": code,
        "logintype": "1"
    }

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "origin": "https://jobzpgl.swufe.edu.cn",
        "referer": "https://jobzpgl.swufe.edu.cn/Job/login/index.html",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    url = "https://jobzpgl.swufe.edu.cn/Job/Login/check.html"

    response = requests.post(url, data=formdata, headers=headers)

    # print(response.json())
    if response.json()['state'] == 0 and response.json()['msg'] == '登陆账号或密码错误':
        return {'code': 0, 'msg': 'error account or password'}
    elif response.json()['state'] == 1:
        return {'code': 1, 'msg': 'success', 'cookies': cookies}
    else:
        return {'code': 5, 'msg': 'error network'}


if __name__ == '__main__':
    login('神州优车股份有限公司', 'szyc2018')