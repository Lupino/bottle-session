bottle-session
==============

A bottle plugin session

        from bottle import run, Bottle 
        from beaker.middleware import SessionMiddleware
        from bottle_session import Plugin
        
        app = Bottle()
        app.install(Plugin())
        
        app.get('/hello')
        def hello():
            # Access the session
            app.session['key']

        session_opts = { 
            'session.type': 'file',
            'session.cookie_expires': 3600,
            'session.data_dir': '/tmp',
            'session.auto': True
        }
        app = SessionMiddleware(app, session_opts)

Platform: any

Classifier: Environment :: Web Environment

Classifier: Intended Audience :: Developers

Classifier: License :: OSI Approved :: MIT License

Classifier: Operating System :: OS Independent

Classifier: Programming Language :: Python

Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content

Classifier: Topic :: Software Development :: Libraries :: Python Modules

Requires: bottle (>=0.9) beaker
