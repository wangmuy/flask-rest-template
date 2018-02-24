# coding: utf-8

# @Time    : 2018/1/17 10:36
# @Author  : wangmuy
# @Contact : wangmuy@gmail.com
# @Desc    :

import logging
from flask import Flask, Blueprint
from flask_cors import CORS
from api.restplus import api
from api import v1
from dbmodel.config import CONFIG as DB_CONFIG


log = logging.getLogger(__name__)
app = Flask(__name__)
ver = v1
db = ver.settings['database']


@app.teardown_appcontext
def shutdown_session(response_or_exc=None):
    """Close the db at the end of the request."""
    global db
    db.get_sess().remove()
    return response_or_exc


def init_app(flask_app):
    flask_app.config.update(dict(
        DATABASE=DB_CONFIG.content['db_sqlite_relative'],
    ))
    flask_app.config.from_envvar('FALSKR_SETTINGS', silent=True)

    global ver
    api.version = ver.settings['version']
    ver.settings['database'].init(flask_app.config['DATABASE'])

    blueprint = Blueprint('api', __name__, url_prefix='/api'+ver.settings['url'])
    CORS(blueprint)
    for ns in ver.settings['namespaces']:
        api.add_namespace(ns)
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)


init_app(app)


def main():
    global app
    app.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
