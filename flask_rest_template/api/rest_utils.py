# coding: utf-8

# @Time    : 2018/1/18 15:14
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from urllib.parse import urlencode
from flask import request
from flask_sqlalchemy import BaseQuery


def paginate_query(query, page, per_page, **kwargs):
    ret_page = BaseQuery.paginate(query, page, per_page, **kwargs)
    if ret_page.has_prev:
        ret_page.prev_link = "{}?{}".format(
            request.base_url, urlencode({'page': ret_page.prev_num, 'per_page': ret_page.per_page}))
    if ret_page.has_next:
        ret_page.next_link = "{}?{}".format(
            request.base_url, urlencode({'page': ret_page.next_num, 'per_page': ret_page.per_page}))
    return ret_page
