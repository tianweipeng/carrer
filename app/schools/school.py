# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import reqparse, Resource, Api
from app.schools import school_spider
from app.errors import BaseError
import importlib

api = Api(school_spider)

# 添加请求参数
parser = reqparse.RequestParser()
# 用户名
parser.add_argument('account')
# 密码
parser.add_argument('password')

# 检查是否注册
class Check(Resource):
    def get(self, school_name):
        args = parser.parse_args()
        # 根据学校名选择引入对应的模块
        path = 'app.schools.' + school_name + '.' + school_name + '_' + 'check.check'
        # 找到模块和模块内的对象
        model_path, class_name = path.rsplit(".", 1)
        # 获取模块
        school_module = importlib.import_module(model_path)
        # 根据学校名选择引入对应的模块,模块的方法
        school_operation = getattr(school_module, class_name)
        account = args.get('account')
        # 执行企业校验操作
        try:
            code = school_operation(account=account)
            return jsonify({'obj': code})
        except Exception as e:
            print(e)
            return BaseError.server_error("error server")

# 企业注册
class Rejister(Resource):
    def post(self, school_name):
        args = parser.parse_args()
        # 根据学校名选择引入对应的模块
        path = 'app.schools.' + school_name + '.' + school_name + '_' + 'rejister.rejister'
        # 找到模块和模块内的对象
        model_path, class_name = path.rsplit(".", 1)
        # 获取模块
        school_module = importlib.import_module(model_path)
        # 根据学校名选择引入对应的模块,模块的方法
        school_operation = getattr(school_module, class_name)
        # 获取企业名称
        account = args.get('account')
        password = args.get('password')
        # 执行学校的登陆操作
        try:
            code = school_operation(account=account, password=password)
            return jsonify({'obj': code})
        except Exception as e:
            print(e)
            return BaseError.server_error("error server")

# 企业登陆
class Login(Resource):
    def post(self, school_name):
        args = parser.parse_args()
        # 根据学校名选择引入对应的模块
        path = "app.schools." + school_name + '.' + school_name + '_' + 'login.login'
        # 找到模块和模块内的对象
        model_path, class_name = path.rsplit(".", 1)
        # 获取模块
        school_module = importlib.import_module(model_path)
        # 获取模块的方法
        school_rejister = getattr(school_module, class_name)
        account = args.get('account')
        password = args.get('password')
        # 执行学校的登陆操作
        try:
            code = school_rejister(account=account, password=password)
            return jsonify({'obj': code})
        except Exception as e:
            print(e)
            return BaseError.server_error("error server")


# 设置路由
api.add_resource(Check, '/check/<school_name>', endpoint='check')