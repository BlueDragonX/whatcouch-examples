
from pyramid.config import Configurator
from pyramid.authentication import RepozeWho1AuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.exceptions import Forbidden
from whatcouch_pyramid.resources import get_root, Root
from whatcouch_pyramid.auth import add_auth
from whatcouch_pyramid.model import init_model

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    init_model(global_config)

    authentication_policy = RepozeWho1AuthenticationPolicy()
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(root_factory=get_root, settings=settings,
        authentication_policy=authentication_policy,
        authorization_policy=authorization_policy)

    config.add_view('whatcouch_pyramid.views.forbidden',
        context=Forbidden)
    config.add_view('whatcouch_pyramid.views.my_view',
        context='whatcouch_pyramid:resources.Root',
        renderer='whatcouch_pyramid:templates/mytemplate.pt')
    config.add_view('whatcouch_pyramid.views.page_public',
        name='',
        context='whatcouch_pyramid:resources.Page',
        renderer='whatcouch_pyramid:templates/page/public.mako')
    config.add_view('whatcouch_pyramid.views.page_public',
        name='public',
        context='whatcouch_pyramid:resources.Page',
        renderer='whatcouch_pyramid:templates/page/public.mako')
    config.add_view('whatcouch_pyramid.views.page_private',
        name='private',
        context='whatcouch_pyramid:resources.Page',
        renderer='whatcouch_pyramid:templates/page/private.mako',
        permission='view')
    config.add_view('whatcouch_pyramid.views.auth_challenge',
        name='challenge',
        context='whatcouch_pyramid:resources.Auth',
        renderer='whatcouch_pyramid:templates/auth/challenge.mako')
    config.add_view('whatcouch_pyramid.views.auth_postlogin',
        name='postlogin',
        context='whatcouch_pyramid:resources.Auth')
    config.add_view('whatcouch_pyramid.views.auth_postlogout',
        name='postlogout',
        context='whatcouch_pyramid:resources.Auth',
        renderer='whatcouch_pyramid:templates/auth/goodbye.mako')
    config.add_static_view('static', 'whatcouch_pyramid:static')
    return add_auth(config.make_wsgi_app())

