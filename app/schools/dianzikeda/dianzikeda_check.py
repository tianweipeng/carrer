# -*- coding: utf-8 -*-

import requests
import json

def check(account):
    # check {1：检查企业是否可用，2：检查用户名是否可用}
    # emp_username 用户名
    # enter_name 企业名

    url = "http://jiuye.uestc.edu.cn/sys/fore.php"

    header = {
        "Host": "jiuye.uestc.edu.cn",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Origin": "http://jiuye.uestc.edu.cn",
        "Connection": "keep-alive",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_1.html"
    }

    param = {
        "op": "empSignUp",
        "callback": "jQuery18308310784259705312_1579238747871"
    }

    data = {
        "check": 2,
        "enter_name": account,
        "emp_username": account
    }

    response = requests.post(url, headers=header, params=param, data=data)
    print(response.text)

    response = json.loads(response.text.split('(',1)[1].rstrip(')'))
    print(response)
    #print(response['s'], response['r'])
    if response['s'] == 0:
        return {'code': 0, 'msg': account + '可注册到电子科大就业网'}
    elif response['s'] == 1:
        return {'code': 0, 'msg': account + '已被注册'}
    else:
        return {'code': 5, 'msg': '网络异常'}

if __name__ == '__main__':
    check('test')