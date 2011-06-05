from whatcouch import setup_couch_auth

def add_auth(app):
    """
    Configure repoze.who and repoze.what middleware for whatcouch and add it
    to the WSGI application.  Called from middleware.py.
    :param app: The WSGI application to add the authentication middleware to.
    :return: The modified WSGI application.
    """
    return setup_couch_auth(app,
        post_login_url='/auth/postlogin',
        post_logout_url='/auth/postlogout',
        login_url='/auth/challenge',
        login_handler='/auth/login',
        logout_handler='/auth/logout')

