# -*- coding: utf-8 -*-

import requests
import json
import os
from app.schools.models import Company
# 注册
def rejister(account, password):
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

    file = company.business_license
    filename = os.path.split(file)[1]
    extension = os.path.splitext(filename)[1]
    filetype ={
        '.jegp': 'image/jpeg',
        '.jpg': 'image/jpeg',
        '.png': 'image/png'
    }
    # 打开文件
    with open(file, 'rb') as f:
        files = {
            "file_type": (None, "1"),
            "emp_organization": (filename, f, filetype[extension])
        }
        response = requests.post(url=url_up, files=files, headers=headers, params=param_up, cookies=cookies)
        print(response.json())
    zuzhijigouzhengshu_address = response.json()['data']


    # 上传营业执照
    filepath = company.business_license
    with open(file, 'rb') as f:
        files = {
            "file_type": (None, "2"),
            "emp_license": (filename, f, filetype[extension])
        }
        response = requests.post(url=url_up, files=files, headers=headers, params=param_up, cookies=cookies)
        print(response.json())
    yingyezhizhao_address = response.json()['data']
    '''

    # 上传的第一页数据
    url = "http://jiuye.uestc.edu.cn/sys/fore.php"

    param_fir = {
        "op": "empSignUp",
        "callback": "jQuery18306914985989217957_1584683816972"
    }

    data_fir = {
        "enter_name": account,
        "emp_username": account,
        "emp_password": password,
        "emp_phone": company.contact_person_phone,
        "emp_email": company.contact_person_email,
        "emp_post": company.contact_person_name,
        "emp_organization": ".. /uploadify/employer/emp_organization/579245524.jpg", # zuzhijigouzhengshu_address
        "emp_license": "../uploadify/employer/emp_license/1579251913.jpg" # yingyezhizhao_address
    }

    headers_fir = {
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_1.html",
        "Host": "jiuye.uestc.edu.cn",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    response_fir = requests.post(url, headers=headers_fir, param=param_fir, data=data_fir, cookies=cookies)
    response_fir = json.loads(response_fir.text.split('(',1)[1].rstrip(')'))
    if response_fir['s'] == 0:
        print('ok')
        company_id = response_fir['id']
    else:
        return {'code': 5, 'msg': '网络异常'}


    # 上传第二页的数据

    headers_sec = {
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_2.html?emplayer_id=" + company_id,
        "Host": "jiuye.uestc.edu.cn",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    param_sec = {
        "op": "empSignUp",
        "callback": "jQuery18306914985989217957_1584683816972"
    }

    kind ={
        1: "机关",
        2: "科研设计单位",
        3: "高等教育单位",
        4: "初中教育单位",
        5: "医疗卫生单位",
        6: "其他事业单位",
        7: "国有企业",
        8: "三资企业（外资企业）",
        9: "其他企业（民营企业）",
        10: "部队",
        11: "农村建制村",
        12: "城镇社区"
    }

    classify = {
        1: "农、林、牧、渔业",
        2: "采矿业",
        3: "制造业",
        4: "电力、热力、燃气及水生产和供应业",
        5: "建筑业",
        6: "批发和零售业",
        7: "交通运输、仓储和邮政业",
        8: "住宿和餐饮业",
        9: "信息传输、软件和信息技术服务业",
        10: "金融业",
        11: "房地产业",
        12: "租赁和商务服务业",
        13: "科学研究和技术服务业",
        14: "水利、环境和公共设施管理业",
        15: "居民服务、修理和其他服务业",
        16: "教育",
        17: "卫生和社会工作",
        18: "文化、体育和娱乐业",
        19: "公共管理、社会保障和社会组织",
        20: "国际组织",
        21: "军队"
    }

    size = {
        1: "50人以下",
        2: "50至100人",
        3: "100至300人",
        4: "300至500人",
        5: "500至1000人",
        6: "1000人以上"
    }

    data_sec = {
        "enter_kind": kind[company.company_property],
        "enter_address": company.company_detail_address,
        "enter_phone": company.company_phone,
        "enter_email": company.contact_person_email,
        "enter_class": classify[company.company_classify],
        "enter_size": size[company.company_scale],
        "enter_page": company.company_website,
        "emp_id": company_id,
        "type": 1
    }

    response_sec = requests.post(url, headers=headers_sec, param=param_sec, data=data_sec, cookies=cookies)
    response_sec = json.loads(response_sec.text.split('(', 1)[1].rstrip(')'))
    if response_sec['s'] == 0:
        print('ok')
    else:
        return {'code': 5, 'msg': '网络异常'}

    # 上传第三页的数据
    headers_thi = {
        "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.uestc.edu.cn/career/register_3.html?emplayer_id=" + company_id,
        "Host": "jiuye.uestc.edu.cn",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }

    data_thi = {
        "emp_intro": "<p>" + company.company_introduce + "<br></p>",
        "emp_id": company_id,
        "type": 2
    }

    response_fir = requests.post(url, headers=headers_fir, param=param_fir, data=data_fir, cookies=cookies)
    response_fir = json.loads(response_fir.text.split('(', 1)[1].rstrip(')'))
    if response_fir['s'] == 0:
        print('ok')

    else:
        return {'code': 5, 'msg': '网络异常'}

    #
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
