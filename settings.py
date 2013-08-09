import os
import resources

DEBUG = False

MONGO_DBNAME = os.environ.get('MONGOHQ_URL', 'superdesk')

SERVER_NAME = 'localhost:5000'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_URL = 'http://localhost:8000/'

DATE_CREATED = 'firstCreated'
LAST_UPDATED = 'versionCreated'

DOMAIN = {
    'items': resources.items,
    'users': resources.users,
}
