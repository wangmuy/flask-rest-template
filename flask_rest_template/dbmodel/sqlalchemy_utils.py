#!/usr/bin/env python
# coding: utf-8

# @Time    : 2017/11/24 16:02
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ClauseElement


class SessionContext(object):
    session = None

    def __init__(self, commitOnExit=False, closeOnExit=True):
        self.commitOnExit = commitOnExit
        self.closeOnExit = closeOnExit

    @staticmethod
    def open_ctx(db, commitOnExit=False, closeOnExit=True):
        ctx = SessionContext(commitOnExit, closeOnExit)
        ctx.open(db)
        return ctx

    def open(self, db):
        engine = create_engine(db, poolclass=NullPool)
        self.session = sessionmaker(bind=engine)()
        return self.session

    def close(self):
        self.session.close()

    def get(self):
        return self.session

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            if self.commitOnExit:
                self.session.commit()
        else:
            self.session.rollback()

        if self.closeOnExit:
            self.session.close()


def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        if defaults:
            params.update(defaults)
        instance = model(**params)
        return instance


def get_autoincrement_column(table_cls):
    columns = table_cls.__table__.columns
    for column in columns.values():
        if type(column.autoincrement) == bool and column.autoincrement is True:
            return column
    return None
