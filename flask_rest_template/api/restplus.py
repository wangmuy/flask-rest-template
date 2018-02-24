# coding: utf-8

# @Time    : 2018/1/17 10:41
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

import logging
import traceback
from flask_restplus import Api


log = logging.getLogger(__name__)

api = Api(version='tbd', doc='/doc/', title='flask-rest-api', description='Flask rest api template')


@api.errorhandler
def default_error_handler(e):
    tb_str = traceback.format_exc()
    log.exception(tb_str)
    return {'message': tb_str}, 500
