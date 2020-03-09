# -*- coding: utf-8 -*-

import requests

# 注册
def rejister(account, password):
    # 上传证件
    url = "https://jobzpgl.swufe.edu.cn/Job/Login/uploadImg"

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

    with open("C:\\Users\\dell\\Desktop\\pkq.jpg", 'rb') as f:
        file = {"excel_file": f}
        response = requests.post(url=url, files=file, headers=header)
        filename = response.json()['url']
        #print(response.json()['url'])

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

    formdata = {
        "name": "2",  # 企业名字（登录名）
        "password": "1111111111",  # 密码
        "password2": "1111111111",  # 确认密码
        "region_level1": 140000,  # 单位所在地，省
        "region_level2": 140100,  # 单位所在地，市
        "region_level3": 140101,  # 单位所在地，区县
        "accept": 2,  # 是否可以接受（或托管）档案
        "accept_hk": 2,  # 是否可以接受（或托管）户口
        "class": 10,  # 单位性质
        "vocation": 11,  # 单位行业
        "bdzqwdwmc": "2",  # 报到证迁住单位名称，写死为2
        "defined": '[{"id": "1", "name": "中国500强"}]',  # 单位分类
        "tyshxydm": "91420000717869088Q",  # 单位18位统一社会信用代码
        "address": "12345678",  # 单位地址（详细地址）
        "tel": "13439367705",  # 单位电话
        "contact": "028-85988267",  # 单位联系人
        "contact_tel": "15810172901",  # 单位联系人手机
        "email": "11 @ 11.com",  # 单位邮箱
        "capital": 1700000,  # 注册资本（万元）
        "excel_file": filename,  # 上传成功返回的图片名
        "gszch_pic": "",
        "describe": "<p>什么东西</p>",  # 单位简介
        "check": 1  # 我已仔细阅读并同意
    }

    response = requests.post(url, headers=headers, data=formdata)

if __name__ == '__main__':
    rejister('2', 'szyc2018')
