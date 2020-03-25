# -*- coding: utf-8 -*-

import requests
from app import scheduler
import  xinancaijing_login
from lxml import html
import xinancaijing_login

from app.schools.models import Company, Company_School, School


'''
# 查找学校id
school_id = School.query.filter(school_name = "xinancaijing").first()
# 查找所有未通过审核的公司id
com = ComStatus.query.filter(school_name == "xinancaijing", status_id == "0").all()
com_id = com.com_id
# 查找对应用户密码
password_all = Password.query.join(Com, Password.com_id == Com.id).filter(Com.id._in(com_id), Com.school_id == school_id).all()
for password_one in password_all:
    username, password = password_one.username, password_one.password
'''
# 查找学校id
school_id = School.query.filter(School.school_name == "xinancaijingdaxue").first()
password_all = Company_School.query.filter(Company_School.rejister_status == "3")

def rejister_reslut():
    url = "https://jobzpgl.swufe.edu.cn/Job/index/index.html"

    heahers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Host": "jobzpgl.swufe.edu.cn",
        "Referer": "https://jobzpgl.swufe.edu.cn/Job/login/index",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
    }

    response = requests.get(url, headers=heahers, cookies=cookies)

    return

def job_result():
    return