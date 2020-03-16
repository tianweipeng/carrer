from app import db
from sqlalchemy import create_engine

class Job(db.Model):
    __tablename__ = 'job'
    # 职位id
    id = db.Column(db.Integer, primary_key=True)
    # 职位名称
    positions = db.Column(db.String(64))
    # 招聘的总岗位数
    jobs_num = db.Column(db.Integer)
    # 招聘对象（应届生1/不限0）
    permissions = db.Column(db.Integer)
    # 职位类型（全职1/实习0）
    recruitment_type = db.Column(db.Integer)
    # 职位分类（参考财大发布职位的分类，例如：销售，市场，财务，等等）
    job_classify = db.Column(db.Integer)
    # 岗位招聘人数
    recruitment_num = db.Column(db.Integer)
    # 招聘主题
    recruitment_theme = db.Column(db.String(64))
    # 学历要求
    record = db.Column(db.Integer)
    # 简历投递邮箱
    send_mail = db.Column(db.String(64))
    # 简历投递网址
    send_website = db.Column(db.String(64))
    # 投递简历开始时间
    start_of_time = db.Column(db.DateTime())
    # 投递简历截至时间
    end_of_time = db.Column(db.DateTime())
    # 专业要求（也是树状结构，或者全部填写不限专业）
    require_major = db.Column(db.Integer)
    # 薪资
    salary = db.Column(db.Float(32))
    # 工作地点(省)
    work_place_province = db.Column(db.Integer)
    # 工作地点(市)
    work_place_city = db.Column(db.Integer)
    # 工作地点(县)
    work_place_county = db.Column(db.Integer)
    # 职位附件（存储位置）
    job_document = db.Column(db.String(64))

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
    # 企业是否接受档案（1为接受，0为不接受）
    accept_archives = db.Column(db.Integer, default=0)
    # 经济类型
    economic_property = db.Column(db.Integer)
    # 企业性质
    company_property = db.Column(db.Integer)
    # 企业所处行业
    company_industry = db.Column(db.Integer)
    # 企业分类
    company_classify = db.Column(db.Integer)
    # 企业隶属部门
    subjection_department = db.Column(db.Integer, default=None)
    # 企业信用代码
    credit_num = db.Column(db.String(64), unique=True)
    # 企业电话
    company_phone = db.Column(db.String(16))
    # 企业联系人
    contact_person_name = db.Column(db.String(32))
    # 企业联系人邮箱
    contact_person_email = db.Column(db.String(64))
    # 企业联系人电话
    contact_person_phone = db.Column(db.String(32))
    #公司规模
    company_scale = db.Column(db.String(16))
    # 企业邮编
    company_code = db.Column(db.String(16))
    # 企业传真
    company_portraiture = db.Column(db.String(32))
    # 注册资金
    registered_capital = db.Column(db.Float(32))
    # 企业官网
    company_website = db.Column(db.String(64))
    # 营业执照（文件）
    business_license = db.Column(db.String(255))
    # 企业介绍
    company_introduce = db.Column(db.Text)
    # 是否注册
    is_registed = db.Column(db.Boolean, default=0)
    # 注册是否通过审核
    is_passed = db.Column(db.Boolean, default=0)

class Tcom(db.Model):
    __tablename__ = "tc"
    # 企业id
    id = db.Column(db.Integer, primary_key=True)
    # 企业名称
    name = db.Column(db.String(64), unique=True)
    # 企业地点(省)
    company_place_province = db.Column(db.Integer)

class Tuser(db.Model):
    __tablename__ = "tu"
    # 企业id
    id = db.Column(db.Integer, primary_key=True)
    # 企业名称
    staff = db.Column(db.String(64), unique=True)
    #性别
    sex = db.Column(db.Integer)
    # 企业id
    com_id = db.Column(db.Integer)