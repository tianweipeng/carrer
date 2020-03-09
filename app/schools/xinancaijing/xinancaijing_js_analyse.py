# -*- coding: utf-8 -*-
import execjs
import os

# 获取js代码
def getJsCode():
    path = os.path.dirname(__file__)
    print(path)
    f = open(path + "\\xinancaijing.js", 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

# 破解密码
def get_password(password_pre):
    js_content = getJsCode()
    ctx = execjs.compile(js_content)
    password_new = ctx.call('changePassword', password_pre)
    return password_new

if __name__ == '__main__':
    print(get_password("szyc2018"))