from .rest_db import api as db_api
from .database import db

settings = {
    'version': '1.0',
    'url': '/v1',
    'namespaces': [db_api],
    'database': db,
}
