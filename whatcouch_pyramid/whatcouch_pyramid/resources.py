
class Resource(dict):
    __name__ = None
    __parent__ = None

    def __init__(self, contents={}):
        dict.__init__(self, contents)
        for k, v in self.iteritems():
            self[k].__name__ = k
            self[k].__parent__ = self

    def __setitem__(self, key, item):
        item.__name__ = key
        item.__parent__ = self
        dict.__setitem__(key, item)

class Root(Resource):
    pass

class Auth(Resource):
    pass

class Page(Resource):
    pass

def get_root(request):
    return Root({
        'auth': Auth(),
        'page': Page()})

