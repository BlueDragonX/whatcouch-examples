"""Setup the whatcouch-quickstart-example application"""
import logging, sys

import pylons.test

from whatcouch_pylons.config.environment import load_environment
from whatcouch_pylons.model import Session
from whatcouch.model import User, Group, Permission
from couchdbkit.loaders import FileSystemDocsLoader

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup whatcouch_pylons here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Add design docs to CouchDB.
    loader = FileSystemDocsLoader(sys.path[0] + '/whatcouch_pylons/_design')
    loader.sync(Session.auth)

    # Add a user, group, and permission to CouchDB.
    user_name = 'admin'
    user_password = 'password'
    group_name = 'administrators'
    perm_name = 'superpowers'

    if len(User.view('whatcouch/user_list', key=user_name)) > 0:
        raise Exception('User already exists.')
    if len(Group.view('whatcouch/group_list', key=group_name)) > 0:
        raise Exception('Group already exists.')
    if len(Permission.view('whatcouch/permission_list', key=perm_name)) > 0:
        raise Exception('Permission already exists.')

    perm = Permission(name=perm_name)
    perm.save()
    group = Group(name=group_name)
    group.permissions.append(perm)
    group.save()
    user = User.create(user_name, user_password)
    user.groups.append(group)
    user.save()

