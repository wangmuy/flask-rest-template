# coding: utf-8

# @Time    : 2018/1/17 10:49
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

import sys
import traceback
import logging
import json
from flask import request, url_for
from flask_restplus import Namespace, Resource, fields

from dbmodel import models, sqlalchemy_utils
from ..rest_models import paginationParser, queryParser
from ..rest_utils import paginate_query
from .rest_models import restModels
from .database import db


log = logging.getLogger(__name__)

api = Namespace('db', description='database rest api')


def _post(cls):
    d = request.get_json()
    # print("json dict: ", d)
    record = cls.TABLE()
    for key in d:
        if hasattr(record, key):
            setattr(record, key, d[key])
    # print("Add Record: ", record)

    try:
        sess = db.get_sess()
        sess.add(record)
        sess.commit()
        ret_code = 200
    except Exception as e:
        traceback.print_stack()
        print("Exception: ", e)
        ret_code = 500

    return '', ret_code


def _edit(table, id_col_name, _id):
    d = request.get_json()
    # print("d=", d)
    sess = db.get_sess()
    record = table.query(sess).filter_by(**{id_col_name: _id}).first()
    if record is None:
        return 'Cannot find record', 500
    # print('before edit: ', record)
    for key in d:
        if hasattr(record, key):
            setattr(record, key, d[key])
    # print('after edit: ', record)
    sess.commit()
    return ''


@api.route('/Album')
class AlbumList(Resource):
    TABLE = models.Album

    @api.expect(paginationParser, validate=True)
    @api.marshal_with(restModels.get_read_multi(TABLE.__tablename__))
    def get(self):
        args = paginationParser.parse_args(request)
        page = args['page']
        per_page = args['per_page']

        q = self.__class__.TABLE.query(db.get_sess())
        if per_page is None:
            ret_page = {'items': q.all()}
        else:
            ret_page = paginate_query(q, page, per_page)
        return ret_page

    @api.expect(restModels.get_write_one(TABLE.__tablename__), validate=True)
    def post(self):
        return _post(self.__class__)


@api.route('/Album/edit/<int:_id>')
class AlbumEdit(Resource):
    TABLE = models.Album
    ID_COLUMN_NAME = sqlalchemy_utils.get_autoincrement_column(TABLE).name

    @api.expect(restModels.get_write_one(TABLE.__tablename__))
    def post(self, _id):
        return _edit(self.TABLE, self.ID_COLUMN_NAME, _id)


@api.route('/Customer')
class CustomerList(Resource):
    TABLE = models.Customer

    @api.expect(queryParser, validate=True)
    @api.marshal_with(restModels.get_read_multi(TABLE.__tablename__))
    def get(self):
        args = queryParser.parse_args(request)
        page = args['page']
        per_page = args['per_page']
        where_clause = args['q']

        q = self.__class__.TABLE.query(db.get_sess())
        if where_clause is not None:
            q = q.filter(where_clause)
        if per_page is None:
            ret_page = {'items': q.all()}
        else:
            ret_page = paginate_query(q, page, per_page)
        return ret_page

    @api.expect(restModels.get_write_one(TABLE.__tablename__), validate=True)
    def post(self):
        return _post(self.__class__)


@api.route('/Customer/edit/<int:_id>')
class CustomerEdit(Resource):
    TABLE = models.Customer
    ID_COLUMN_NAME = sqlalchemy_utils.get_autoincrement_column(TABLE).name

    @api.expect(restModels.get_write_one(TABLE.__tablename__))
    def post(self, _id):
        return _edit(self.TABLE, self.ID_COLUMN_NAME, _id)


@api.route('/Employee')
class EmployeeList(Resource):
    TABLE = models.Employee

    @api.expect(queryParser, validate=True)
    @api.marshal_with(restModels.get_read_multi(TABLE.__tablename__))
    def get(self):
        args = queryParser.parse_args(request)
        page = args['page']
        per_page = args['per_page']
        where_clause = args['q']

        q = self.__class__.TABLE.query(db.get_sess())
        if where_clause is not None:
            q = q.filter(where_clause)
        if per_page is None:
            ret_page = {'items': q.all()}
        else:
            ret_page = paginate_query(q, page, per_page)
        return ret_page

    @api.expect(restModels.get_write_one(TABLE.__tablename__), validate=True)
    def post(self):
        return _post(self.__class__)


@api.route('/Employee/edit/<int:_id>')
class EmployeeEdit(Resource):
    TABLE = models.Employee
    ID_COLUMN_NAME = sqlalchemy_utils.get_autoincrement_column(TABLE).name

    @api.expect(restModels.get_write_one(TABLE.__tablename__))
    def post(self, _id):
        return _edit(self.TABLE, self.ID_COLUMN_NAME, _id)


@api.route('/Invoice')
class InvoiceList(Resource):
    TABLE = models.Invoice

    @api.expect(paginationParser, validate=True)
    @api.marshal_with(restModels.get_read_multi(TABLE.__tablename__))
    def get(self):
        args = paginationParser.parse_args(request)
        page = args['page']
        per_page = args['per_page']

        q = self.__class__.TABLE.query(db.get_sess())
        ret_page = paginate_query(q, page, per_page, max_per_page=1000)
        return ret_page

    @api.expect(restModels.get_write_one(TABLE.__tablename__), validate=True)
    def post(self):
        return _post(self.__class__)


@api.route('/Invoice/edit/<int:_id>')
class InvoiceEdit(Resource):
    TABLE = models.Invoice
    ID_COLUMN_NAME = sqlalchemy_utils.get_autoincrement_column(TABLE).name

    @api.expect(restModels.get_write_one(TABLE.__tablename__))
    def post(self, _id):
        return _edit(self.TABLE, self.ID_COLUMN_NAME, _id)


@api.route('/Track')
class TrackList(Resource):
    TABLE = models.Track

    @api.expect(paginationParser, validate=True)
    @api.marshal_with(restModels.get_read_multi(TABLE.__tablename__))
    def get(self):
        args = paginationParser.parse_args(request)
        page = args['page']
        per_page = args['per_page']

        q = self.__class__.TABLE.query(db.get_sess())
        ret_page = paginate_query(q, page, per_page, max_per_page=1000)
        return ret_page

    @api.expect(restModels.get_write_one(TABLE.__tablename__), validate=True)
    def post(self):
        return _post(self.__class__)


@api.route('/Track/edit/<int:_id>')
class TrackEdit(Resource):
    TABLE = models.Track
    ID_COLUMN_NAME = sqlalchemy_utils.get_autoincrement_column(TABLE).name

    @api.expect(restModels.get_write_one(TABLE.__tablename__))
    def post(self, _id):
        return _edit(self.TABLE, self.ID_COLUMN_NAME, _id)
