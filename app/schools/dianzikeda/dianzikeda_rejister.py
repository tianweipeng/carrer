# -*- coding: utf-8 -*-

import requests
import os
from app.schools.models import Company
# 注册
def rejister(account):
    # 获取企业信息
    company = Company.query.filter(Company.name == account).first()

    # 获取cookie
    url_cookie = "http://jiuye.uestc.edu.cn/sys/fore.php"

    param_cookie = {
        'ob': 'checkUserStatus',
        'callback': 'jQuery18306914985989217957_1584683816972'
    }

    header_cookie = {
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://jiuye.uestc.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_1.html",
        "Host": "jiuye.uestc.edu.cn"
    }
    response_cookie = requests.post(url_cookie, headers=header_cookie, param=param_cookie)
    cookies = response_cookie.cookies.get_dict()

    # 上传组织机构证书
    '''
    url_up = "http://jiuye.uestc.edu.cn/sys/fore.php"

    param_up = {"op": "licenseUpload"}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "Origin": "http://jiuye.uestc.edu.cn",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_1.html",
        "Upgrade-Insecure-Requests": "1"
    }

    filepath = company.business_license
    filepath, tmpfilename = os.path.split(filepath)
    shotname, extension = os.path.splitext(tmpfilename)
    full_file_name = shotname + extension
    filetype ={
        '.jegp': 'image/jpeg',
        '.jpg': 'image/jpeg',
        '.png': 'image/png'
    }
    # 打开文件
    with open(filepath, 'rb') as f:
        pass
    files = {
        "file_type": (None, "1"),
        "emp_organization": (full_file_name, f, filetype[extension])
    }
    response = requests.post(url=url_up, files=files, headers=headers, params=param_up, cookies=cookies)
    # print(response.json())
    zuzhijigouzhengshu_address = response.json()['data']


    # 上传营业执照
    filepath = company.business_license
    with open(filepath, 'rb') as f:
        pass
    files = {
        "file_type": (None, "2"),
        "emp_license": (full_file_name, f, filetype[extension])
    }
    response = requests.post(url=url_up, files=files, headers=headers, params=param_up, cookies=cookies)
    print(response.json())
    yingyezhizhao_address = response.json()['data']
    '''



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

    # response = requests.post(url, data=data, headers=headers)
    # response = response.text.split(':')[2].split(',')[0].strip('"')
    #
    # if response == 'dwusertrue':
    #     return {'code': 0, 'msg': 'already rejistered'}
    # elif response == 'true':
    #     return {'code': 1, 'msg': 'not rejister'}
    # else:
    #     return {'code': 2, 'msg': 'error network'}

if __name__ == '__main__':
    rejister('航天信息股份有限公司')
