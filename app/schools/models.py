# -*- coding: utf-8 -*-

from app import db

class Job(db.Model, db.Session):
    # 表名
    __tablename__ = "job"
    # 岗位id
    id = db.Column(db.Integer, primary_key=True)
    # 招聘主题
    theme = db.Column(db.String(64))
    # 招聘的总岗位数
    job_num = db.Column(db.Integer)
    # 本次招聘总人数
    total_num = db.Column(db.Integer)
    # 简历投递邮箱
    send_mail = db.Column(db.String(64))
    # 简历投递网址
    send_website = db.Column(db.String(64))
    # 投递简历开始时间
    start_of_time = db.Column(db.DateTime())
    # 投递简历截至时间
    end_of_time = db.Column(db.DateTime())
    # 职位描述
    job_description = db.Column(db.Text)
    # 职位附件（存储位置）
    job_document = db.Column(db.String(64))
    # 对应公司id
    company_id = db.Column(db.Integer)
    # 对应学校id
    school_id = db.Column(db.Integer)

    # 返回可读字符串，便于调试和测试
    def __repr__(self):
        return '<Job %r>' % self.theme

class Station(db.Model):
    __tablename__ = 'station'
    # 职位id
    id = db.Column(db.Integer, primary_key=True)
    # 岗位名称
    position = db.Column(db.String(64))
    # 招聘对象（应届生1/不限0）
    permissions = db.Column(db.Integer)
    # 职位类型（全职1/实习0）
    recruitment_type = db.Column(db.Integer)
    # 岗位分类1（参考财大发布职位的分类，例如：销售，市场，财务，等等）
    station_classify_one = db.Column(db.Integer)
    # 岗位分类2（参考财大发布职位的分类，例如：销售，市场，财务，等等）
    station_classify_two = db.Column(db.Integer)
    # 岗位招聘人数
    recruitment_num = db.Column(db.Integer)
    # 学历要求
    record = db.Column(db.Integer)
    # 专业要求（也是树状结构，或者全部填写不限专业）
    require_major = db.Column(db.Integer)
    # 薪资
    salary = db.Column(db.String(32))
    # 工作地点(省)
    work_place_province = db.Column(db.Integer)
    # 工作地点(市)
    work_place_city = db.Column(db.Integer)
    # 工作地点(县)
    work_place_county = db.Column(db.Integer)
    # 对应的职位id
    job_id = db.Column(db.Integer)

    # 返回可读字符串，便于调试和测试
    def __repr__(self):
        return '<Station %r>' % self.position

class Company(db.Model):
    # 表名
    __tablename__ = "company"
    # 企业id
    id = db.Column(db.Integer, primary_key=True)
    # 企业名称
    name = db.Column(db.String(64), unique=True)
    # 企业地点(省)
    company_place_province = db.Column(db.Integer)
    # 企业地点(市)
    company_place_city = db.Column(db.Integer)
    # 企业地点(县)
    company_place_county = db.Column(db.Integer)
    # 企业详细地址
    company_detail_address = db.Column(db.String(255))
    # 企业是否接受档案（1为接受，0为不接受）
    accept_archives = db.Column(db.Integer, default=None)
    # 经济类型 （国有，私有，三资台办，三资外企，参考西交注册页面）
    economic_property = db.Column(db.Integer)
    # 企业性质（机关，科研，高等教育，部队，国有，三资，等等）
    company_property = db.Column(db.Integer)
    # 企业所处行业一级菜单（农林牧渔业，采矿，制造，建筑，等等）
    company_industry_one = db.Column(db.Integer)
    # 企业所处行业二级菜单（以及行业下的子行业）
    company_industry_two = db.Column(db.Integer)
    # 企业分类（世界500强， 中国500强，上市，等等）
    company_classify = db.Column(db.Integer)
    # 企业隶属部门
    subjection_department = db.Column(db.Integer, default=None)
    # 企业信用代码
    credit_num = db.Column(db.String(64), unique=True)
    # 企业电话
    company_phone = db.Column(db.String(32))
    # 企业联系人
    contact_person_name = db.Column(db.String(32))
    # 企业联系人邮箱
    contact_person_email = db.Column(db.String(64))
    # 企业联系人电话
    contact_person_phone = db.Column(db.String(32))
    # 公司规模
    company_scale = db.Column(db.Integer)
    # 企业邮编
    company_code = db.Column(db.Integer)
    # 企业传真
    company_portraiture = db.Column(db.String(32))
    # 注册资金
    registered_capital = db.Column(db.Float(32))
    # 企业官网
    company_website = db.Column(db.String(64))
    # 营业执照（文件存储位置）
    business_license = db.Column(db.String(255))
    # 营业执照有效期
    expire_date = db.Column(db.DateTime())
    # 成立日期
    set_up_date = db.Column(db.DateTime())
    # 企业介绍
    company_introduce = db.Column(db.Text)
    # 是否注册到学校
    is_registed = db.Column(db.Integer, default=0)
    # 注册是否通过审核
    is_passed = db.Column(db.Integer, default=0)
    # 注册是否审核中
    if_passed = db.Column(db.Integer, default=0)

    # 返回可读字符串，便于调试和测试
    def __repr__(self):
        return '<Company %r>' % self.name