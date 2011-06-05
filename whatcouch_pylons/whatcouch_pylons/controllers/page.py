import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from whatcouch_pylons.lib.base import BaseController, render
from repoze.what.plugins.pylonshq import ActionProtector as authorize
from repoze.what.predicates import not_anonymous

log = logging.getLogger(__name__)

class PageController(BaseController):

    def index(self):
        """
        Display the page index.
        """
        return render('/page/index.html')

    def public(self):
        """
        Display a publicly accessible page.
        """
        return render('/page/public.html')

    @authorize(not_anonymous())
    def private(self):
        """
        Display a page protected by whatcouch.
        """
        return render('/page/private.html')

