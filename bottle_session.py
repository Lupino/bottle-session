__author__ = "Li Meng Jun"
__version__ = '0.0.1'
__license__ = 'MIT'

### CUT HERE (see setup.py)

from bottle import request


class SessionPlugin(object):
    name = 'session'

    def __init__(self):
        self.app = None

    def setup(self, app):
        self.app = app
        self.app.add_hook('before_request', self.load_session)
        self.app.add_hook('after_request', self.set_session)
        
    def load_session(self):
        self.app.session = request.environ.get('beaker.session', {})

    def set_session(self):
        pass

    def apply(self, callback, context):
        return callback


Plugin = SessionPlugin
