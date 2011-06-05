import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from whatcouch_pylons.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def challenge(self):
        """
        This action will display a login form to the user.  It checks the value
        of login_counter to determine if an attempt was already made to log in
        and displays an error message if there was.
        """
        c.error = ''
        c.login_counter = request.environ.get('repoze.who.logins')
        c.came_from = request.params.get('came_from') or url('/')
        if c.login_counter > 0:
            c.error = 'Invalid username or password.'
        return render('/auth/challenge.html')

    def postlogin(self):
        """
        The user is redirected to this action on a successful login.  It
        first checks to ensure the user is actually logged in, then
        redirects accordingly.
        """
        identity = request.environ.get('repoze.who.identity')
        came_from = request.params.get('came_from') or url('/')
        if not identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect(url(controller='auth', action='challenge', came_from=came_from, __logins=login_counter))
        else:
            userid = request.environ.get('repoze.who.userid')
            redirect(url(str(came_from)))

    def postlogout(self):
        """
        The user is redirected to this action on logout.  It simply displays
        a page informing them that they have logged in, giving them the
        option to return to their previous page or log back in.
        """
        came_from = request.params.get('came_from')
        c.came_from = came_from
        return render('/auth/goodbye.html')

