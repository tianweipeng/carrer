# -*- coding: utf-8 -*-

import requests
from app.schools.models import Company

# 检查企业是否存在
def check(account):
    url = "http://jiuye.swjtu.edu.cn/eweb/dwr/call/plaincall/jygldwr.isValidateDwxx.dwr"

    headers = {
        "Host": "jiuye.swjtu.edu.cn",
        "Accept": "*/*",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Content-Type": "text/plain"
    }

    # 获取企业信息
    company = Company.query.filter(Company.name == account).first()

    formdata = {
        "callCount": "1",
        "page": "/eweb/jygl/jyglext.so?type=dwzc",
        "httpSessionId": "",
        "scriptSessionId": "57A0843112C091B0BFCCEE26EA9F64BF886",
        "c0-scriptName": "jygldwr",
        "c0-methodName": "isValidateDwxx",
        "c0-id": "0",
        "c0-param0": "string:Bczoygd2fM6bfagjF8ZNRt",
        "c0-param1": "string:" + account,
        "c0-param2": "string:" + company.credit_num,
        "c0-param3": "string:" + company.contact_person_email,
        "c0-param4": "string:xzDwxx",
        "c0-param5": "boolean:false",
        "batchId": "2"
    }

    response = requests.post(url, headers=headers, data=formdata)
    if 'dwmcResult:"dwusertrue"' in response.text:
        return {'code': 0, 'msg': account + '已被注册'}
    elif 'zzjgdmResult:"zzjgdmfalse"' in response.text:
        return {'code': 2, 'msg': account + '的企业信用代码已被注册'}
    elif 'zpbmemailResult:"dwzhfalse"' in response.text:
        return {'code': 3, 'msg': account + "登陆西南交大的email"+ "已被使用"}
    elif 'zpbmemailResult:"true"' in response.text and 'dwmcResult:"true"' in response.text and 'zzjgdmResult:"true"' in response.text:
        # print(1)
        return {'code': 1, 'msg': account + '可注册'}
    else:
        return {'code': 5, 'msg': '网络异常'}

if __name__ == '__main__':
    # check('神州优车股份有限公司', 'szyc2018')
    print(check('神州优车股份有限公')['code'])