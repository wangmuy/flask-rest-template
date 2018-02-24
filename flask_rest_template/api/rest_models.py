# coding: utf-8

# @Time    : 2018/1/17 11:10
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from sqlalchemy.sql import sqltypes
from flask_restplus import fields, reqparse
from api.restplus import api


paginationParser = reqparse.RequestParser()
paginationParser.add_argument("page", type=int, required=False, default=1, help="Page number")
paginationParser.add_argument("per_page", type=int, required=False, help="Number of items per page")

queryParser = paginationParser.copy()
queryParser.add_argument("q", help="Query where clause")

pagination = api.model('Pagination', {
    'page': fields.Integer(description='Page number'),
    'per_page': fields.Integer(description='Number of items per page'),
    'total': fields.Integer(description='Total number of items'),
    'prev_link': fields.String(description='url of previous page'),
    'next_link': fields.String(description='url of next page'),
})


_mapping = {
    sqltypes.Integer: fields.Integer,
    sqltypes.String: fields.String,
    sqltypes.Boolean: fields.Boolean,
    sqltypes.Date: fields.Date,
    sqltypes.DateTime: fields.DateTime,
    sqltypes.Float: fields.Float,
}

_model_read_one = {}
_model_read_multi = {}
_model_write_one = {}
_model_write_multi = {}


def get_model_write_one(table_name):
    return _model_write_one[table_name]


def get_model_write_multi(table_name):
    return _model_write_multi[table_name]


def get_model_read_one(table_name):
    return _model_read_one[table_name]


def get_model_read_multi(table_name):
    return _model_read_multi[table_name]


def add_table_model(table_cls):
    global _mapping
    global _model_write_one, _model_write_multi
    global _model_read_one, _model_read_multi
    table_name = table_cls.__tablename__
    columns = table_cls.__table__.columns

    read_fields = {
        key: _mapping[type(columns[key].type)](required=True)
        for key in columns.keys() if type(columns[key].type) in _mapping
    }
    write_fields = read_fields.copy()
    for col_name, column in columns.items():
        if type(column.autoincrement) == bool and column.autoincrement is True:
            # print('removing autoincrement field ' + table_name + '.' + column.name)
            write_fields.pop(col_name)

    write_one = api.model(table_name + '_w', write_fields)
    _model_write_one[table_name] = write_one
    _model_write_multi = api.inherit(table_name + '_list_w', pagination, {
        'items': fields.List(fields.Nested(write_one), required=True)
    })

    _model_read_one[table_name] = api.model(table_name, read_fields)
    _model_read_multi[table_name] = api.inherit(table_name + '_list', pagination, {
        'items': fields.List(fields.Nested(_model_read_one[table_name]), required=True)
    })
