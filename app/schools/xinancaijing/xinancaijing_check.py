# -*- coding: utf-8 -*-

import requests
from app.schools.models import Company

# 检查企业是否存在
def check(account):
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

    # 获取企业信息
    company = Company.query.filter(Company.name == account).first()
    formdata = {
        "name": account,  # 登录名
        "accept": "2",
        "accept_hk": "2",
        "tyshxydm": company.credit_num,
        "check": "1"
    }

    response = requests.post(url, headers=headers, data=formdata)
    # print(response.json())
    if response.json()['state'] == 200:
        return {'code': 0, 'msg': response.json()['msg']}
    else:
        return {'code': 5, 'msg': '网络异常'}


if __name__ == '__main__':
    # check_if_rejisterd('神州优车股份有限公司', 'szyc2018')
    check('神州优车股份有限公司')