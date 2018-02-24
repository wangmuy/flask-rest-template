# coding: utf-8

# @Time    : 2018/1/10 15:49
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    : https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file

import os
import json


class Config:
    content = None

    def __init__(self, file):
        with open(file, 'r') as f:
            self.content = json.load(f)

    @staticmethod
    def load(file):
        conf = Config(file)
        return conf

    @staticmethod
    def save(content, file):
        with open(file, 'w') as f:
            json.dump(content, f)


CONFIG = Config.load(os.path.dirname(os.path.realpath(__file__)) + '/config.json')
