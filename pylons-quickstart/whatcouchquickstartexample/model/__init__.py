from couchdbkit import Server
from whatcouch.model import init_model as init_whatcouch_model

class CouchSession:

    def __init__(self):
        """
        Constructor.  Creates a new CouchSession object.
        """
        self.uri_key = 'couch.uri'

    def configure(self, config):
        """
        Configure the session.
        :param config: Pylons config dict.
        """
        if self.uri_key in config:
            """
            If a URI was provided in the config file, use it to configure
            the CouchDB connection.
            """
            self.server = Server(config[self.uri_key])
        else:
            """
            Otherwise it defaults to CouchDB's default, which is localhost.
            """
            self.server = Server()
        """
        Use the new session to initialize the whatcouch model.  We will
        use the 'auth' database by default.
        """

def init_model(config):
    """
    Initialize the CouchDB models.  Called from environment.py during
    app startup.
    :param config: The Pylons config dict.
    """
    Session.configure(config)
    db_name = 'auth'
    db_key = 'whatcouch.db'
    if db_key in config:
        """
        If a db name was provided in the config file we'll use it intead.
        """
        db_name = config[db_key]
    Session.auth = Session.server[db_name]
    init_whatcouch_model(Session.auth)

Session = CouchSession()

