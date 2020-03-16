# -*- coding: utf-8 -*-

import requests
from app.schools.models import Company


# 注册
def rejister(account, password):

    # 查找企业信息
    company = Company.query.filter(Company.name == account).first()

    # 上传证件
    upload_url = "https://jobzpgl.swufe.edu.cn/Job/Login/uploadImg"

    header = {
        'authority': "jobzpgl.swufe.edu.cn",
        "method": "POST",
        "path": "/Job/Login/uploadImg",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "origin": "https://jobzpgl.swufe.edu.cn",
        "referer": "https://jobzpgl.swufe.edu.cn/job/login/register.html",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    # 打开需上传的文件
    # with open(company.business_license, 'rb') as f:
    # with open("C:\\Users\\twp\\Desktop\\AAAA.jpg", 'rb') as f:
        # file = {"excel_file": f}
        # response = requests.post(url=upload_url, files=file, headers=header)
        # filename = response.json()['url']
        # print(response.json()['url'])


    # 注册
    url = "https://jobzpgl.swufe.edu.cn/Job/Login/register"

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "origin": "https://jobzpgl.swufe.edu.cn",
        "referer": "https://jobzpgl.swufe.edu.cn/job/login/register.html",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    defined = {1: "中国500强", 2: "世界500强", 3: "上市", 4: "其他"}

    formdata = {
        "name": company.name,  # 企业名字（登录名）
        "password": password,  # 密码
        "password2": password,  # 确认密码
        "region_level1": company.company_place_province,  # 单位所在地，省
        "region_level2": company.company_place_city,  # 单位所在地，市
        "region_level3": company.company_place_county,  # 单位所在地，区县
        "accept": 2,  # 是否可以接受（或托管）档案
        "accept_hk": 2,  # 是否可以接受（或托管）户口
        "class": company.company_property,  # 单位性质（机关，科研，高等教育，部队，国有，三资，等等）
        "vocation": company.company_industry_one,  # 单位行业
        "defined": [{"id": company.company_classify, "name": defined[company.company_classify]}],  # 单位分类(1,中国500强，2世界500强，3上市，4其他)
        "tyshxydm": company.credit_num,  # 单位18位统一社会信用代码
        "address": company.company_detail_address,  # 单位地址（详细地址）
        "tel": company.company_phone,  # 单位电话
        "contact": company.contact_person_name,  # 单位联系人
        "contact_tel": company.contact_person_phone,  # 单位联系人手机
        "email": company.contact_person_email,  # 单位邮箱
        "capital": company.registered_capital,  # 注册资本（万元）
        "excel_file": "filename",  # 上传成功返回的图片名
        "gszch_pic": "",
        "describe": "<p>" + company.company_introduce + "</p>",  # 单位简介
        "check": 1  # 我已仔细阅读并同意
    }

    print(formdata)
    # response = requests.post(url, headers=headers, data=formdata)


if __name__ == '__main__':
    from app import create_app

    app = create_app('default')
    app_context = app.app_context()
    app_context.push()
    rejister('北京网聘', 'szyc2018')
