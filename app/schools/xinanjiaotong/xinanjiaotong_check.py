# -*- coding: utf-8 -*-

import requests, re

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
        "c0-param2": "string:",
        "c0-param3": "string:",
        "c0-param4": "string:xzDwxx",
        "c0-param5": "boolean:false",
        "batchId": "2"
    }

    response = requests.post(url, headers=headers, data=formdata)
    print(re.search('zpbmemailResult:"true",dwmcResult:"dwusertrue",zzjgdmfjResult:"true",zzjgdmResult:"true"', response.text).span())
    print(response.text)


if __name__ == '__main__':
    # check('神州优车股份有限公司', 'szyc2018')
    check('神州优车股份有限公司')