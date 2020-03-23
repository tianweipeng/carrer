# -*- coding: utf-8 -*-

import requests
import os
from lxml import html
import time
from PIL import Image
from app.schools.models import Company
import xinanjiaotong_check

# 注册
def rejister(account, password):
    # 获取cookie(西郊注册需要提交验证码，所以先获取cookie)
    url_cookie = "http://jiuye.swjtu.edu.cn/eweb/jygl/zpfw.so"
    header_cookie = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/index.so",
        "Host": "jiuye.swjtu.edu.cn"
    }
    response_cookie = requests.post(url_cookie, headers = header_cookie)
    cookies = response_cookie.cookies.get_dict()
    # print(cookies)

    # 西交注册上传时，有一个refid，需先获取此id
    url_re = "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so"
    header_re = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/zpfw.so",
        "host": "jiuye.swjtu.edu.cn"
    }

    param = {"type": "dwzc"}
    response_re = requests.get(url_re, headers=header_re, params=param, cookies=cookies)
    etree = html.etree
    content = etree.HTML(response_re.text)
    refid = content.xpath("/html/body/div[4]/div/div/form/input[2]/@value")[0]
    print(refid)

    # 获取企业信息
    company = Company.query.filter(Company.name == account).first()

    # 上传
    '''
    url_up = "http://jiuye.swjtu.edu.cn/eweb/servlet/resuploadnew"
    header_up = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc"
    }
    file = company.business_license
    filename = os.path.split(file)[1]
    extension = os.path.splitext(filename)[1]
    filetype = {
        '.jegp': 'image/jpeg',
        '.jpg': 'image/jpeg',
        '.png': 'image/png'
    }
    # 打开文件
    with open(file, 'rb') as f:
        files = {'refid':(None, refid),'reftype':(None,'zzjgdmzsmj'),'mdbFiles':(filename, f, filetype[extension])}
        response_up = requests.post(url_up, headers=header_up, files=files, cookies=cookies)
    print(response_up.json())
    '''

    # 验证上传的二进制文件
    # print(requests.Request('POST', url_up, headers=header_up, files=files, cookies=cookies).prepare().body.decode('ascii'))
    # text = reponse.text
    # print (text)

    # 注册
    # 获取验证码
    url_code = "http://jiuye.swjtu.edu.cn/eweb/wfc_r4d.so?type=r4d"
    header_code = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "image/webp,*/*",
        "Host": "jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc"
    }
    response_code = requests.get(url_code, header=header_code, cookies=cookies)
    # 将验证码保存到本地
    with open("C:\\Users\\dell\\Desktop\\test.jpg", 'wb') as f:
        f.write(response_code.content)
        f.close()
    time.sleep(3)
    im = Image.open('C:\\Users\\dell\\Desktop\\test.jpg')
    # 显示图片，目前是显示，之后会加入自动识别
    im.show()
    code = input("input:")

    # 发送注册请求
    url = "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzcPost"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Origin": "http://jiuye.swjtu.edu.cn",
        "Referer": "http://jiuye.swjtu.edu.cn/eweb/jygl/jyglext.so?type=dwzc",
        "host": "jiuye.swjtu.edu.cn"
    }
    formdata = {
        "xxid": "10613", # 固定id
        "dwid": refid,  # 系统生成的refid
        "dwmc": company.name, # 单位名称
        "zzjgdm": company.credit_num, # 企业信用代码
        "zzjgdmzyxq": company.expire_date,  # 营业执照注册有效期
        "szsf": company.company_place_province,  # 省
        "szs": company.company_place_city,  # 地市
        "szx": company.company_place_county,  # 区县
        "xxdz": company.company_detail_address,  # 企业详细地址
        "xzyj": company.company_property,  # 单位性质（机关，科研，高等教育，部队，国有，三资，等等）
        "hyyj": company.company_industry_one,  # 单位行业
        "hyej": company.company_industry_two,  # 单位行业2
        "jjlx": company.economic_property,  # 单位经济类型
        "mdbFiles": "",  # 上传的证书（为空即可）
        "dwjs": company.company_introduce,  # 单位介绍
        "zpbmemail": company.contact_person_email,  # 登录邮箱（登陆用）
        "pwd": password,  # 密码
        "pwdAgain": password,  # 确认密码
        "lxrmc": company.contact_person_name,  # 联系人姓名
        "lxrsj": company.contact_person_phone,  # 联系人手机
        "shbm": "10613.jyzx",  # 审核单位（10613.jyzx为招生就业处（成都校区））
        "hkqclb": "03",  # 户口迁入类别（03为不解决）
        "dazjlb": "03",  # 档案转寄类别（03为不解决）
        "vpwd": code  # 验证码
    }

    email_pass = xinanjiaotong_check.check(account)
    if email_pass['code'] == 1:
        response = requests.post(url=url, headers=header, data=formdata, cookies=cookies)
        etree = html.etree
        response_content = etree.HTML(response.text)
        result = response_content.xpath("/html/body/div[4]/div/div/span[2]")
        # print(response.text)
        if result == "单位注册成功,请等待管理员的审核,你也可以登录系统查看审核信息！":
            return {'code': 0, 'msg': result}
        else:
            return {'code': 5, 'msg': '网络异常'}
    else:
        return email_pass


if __name__ == '__main__':
    rejister("北京网聘","aabbcc123")