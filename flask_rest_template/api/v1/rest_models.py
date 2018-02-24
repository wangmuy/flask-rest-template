# coding: utf-8

# @Time    : 2018/1/17 11:42
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

from api.rest_models import *
from dbmodel import models


class RestModels:
    def __init__(self):
        add_table_model(models.Album)
        add_table_model(models.Artist)
        add_table_model(models.Customer)
        add_table_model(models.Employee)
        add_table_model(models.Genre)
        add_table_model(models.Invoice)
        add_table_model(models.InvoiceLine)
        add_table_model(models.MediaType)
        add_table_model(models.Playlist)
        add_table_model(models.PlaylistTrack)
        add_table_model(models.Track)

    def get_read_one(self, table_name):
        return get_model_read_one(table_name)

    def get_read_multi(self, table_name):
        return get_model_read_multi(table_name)

    def get_write_one(self, table_name):
        return get_model_write_one(table_name)

    def get_write_multi(self, table_name):
        return get_model_write_multi(table_name)


restModels = RestModels()
