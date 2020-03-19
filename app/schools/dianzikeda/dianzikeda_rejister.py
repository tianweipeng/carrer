# -*- coding: utf-8 -*-
import requests


# 登陆方法

def dianke_rejister():
    url = "http://jiuye.uestc.edu.cn/sys/fore.php"

    param = {
        "op": "empSignUp",
        "callback": "jQuery18304668336371149584_1579245558863"
    }

    data = {
        "enter_name": 112,
        "emp_username": 1123,
        "emp_password": "Abc123456",
        "emp_phone": "15972032702",
        "emp_email": "guojing3 @ crccre.cn",
        "emp_post": "郭菁",
        "emp_organization": ".. /uploadify/employer/emp_organization/579245524.jpg",
        "emp_license": "../uploadify/employer/emp_license/1579251913.jpg"
    }

    headers = {
        "accept": "*/*",
        "origin": "http://jiuye.swjtu.edu.cn",
        "referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc",
        "user-agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    url = "http://jiuye.swjtu.edu.cn/eweb/dwr/call/plaincall/jygldwr.isValidateDwxx.dwr"

    response = requests.post(url, data=formdata, headers=headers)
    response = response.text.split(':')[2].split(',')[0].strip('"')

    if response == 'dwusertrue':
        return {'code': 0, 'msg': 'already rejistered'}
    elif response == 'true':
        return {'code': 1, 'msg': 'not rejister'}
    else:
        return {'code': 2, 'msg': 'error network'}

if __name__ == '__main__':
    check('航天信息股份有限公司')
