
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

def my_view(context, request):
    return {'project':'whatcouch_pyramid'}

def forbidden(context, request):
    return Response('Authentication Required', status=401)

def page_public(context, request):
    return {}

def page_private(context, request):
    return {}

def auth_challenge(context, request):
    counter = request.environ.get('repoze.who.logins')
    error = ''
    if counter > 0:
        error  = 'Invalid username or password.'
    return {
        'error': error,
        'login_counter': counter,
        'came_from': request.params.get('came_from') or '/'}

def auth_postlogin(context, request):
    identity = request.environ.get('repoze.who.identity')
    came_from = request.params.get('came_from') or '/'
    if not identity:
        print "no identity, redirect to /auth/challenge"
        login_counter = request.environ.get('repoze.who.logins', 0) + 1
        return HTTPFound(location='/auth/challenge')
    else:
        print "identity found, redirect to %s" % came_from
        return HTTPFound(location=came_from)

def auth_postlogout(context, request):
    return {'came_from': request.params.get('came_from')}

