# coding: utf-8

# @Time    : 2018/1/17 12:37
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dbmodel import models

class Database:
    models = models

    def init(self, path):
        self.engine = create_engine(path, convert_unicode=True, pool_recycle=1800)
        self.db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=self.engine))

    def get_sess(self):
        return self.db_session

db = Database()
