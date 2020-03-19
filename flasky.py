# -*- coding: utf-8 -*-

import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

#添加测试模块，无法使用ide的debug模式启动
# @app.cli.command()
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.run(debug=True)