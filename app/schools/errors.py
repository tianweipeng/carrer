# -*- coding: utf-8 -*-

from flask import request, jsonify, render_template
from app.errors import BaseError
from . import school_spider
from app.exceptions import ValidationError

# 对school蓝本生效
@school_spider.errorhandler(ValidationError)
def validation_error(e):
    return BaseError.bad_request(e.args[0])

# 将原有的404页面转为json ，如果请求头接受html，则返回404页面（这里没有写404页面）
@school_spider.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404
