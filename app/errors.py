# -*- coding: utf-8 -*-

from flask import jsonify

class BaseError():

    def bad_request(message):
        response = jsonify({'error': 'bad request', 'message': message})
        response.status_code = 400
        return response


    def unauthorized(message):
        response = jsonify({'error': 'unauthorized', 'message': message})
        response.status_code = 401
        return response


    def forbidden(message):
        response = jsonify({'error': 'forbidden', 'message': message})
        response.status_code = 403
        return response

    def server_error(message):
        response = jsonify({'error': 'server', 'message': message})
        response.status_code = 500
        return response