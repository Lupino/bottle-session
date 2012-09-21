bottle-session
==============

A session plugin for bottle

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
