"""Setup the whatcouch-quickstart-example application"""
import logging, sys

import pylons.test

from whatcouchquickstartexample.config.environment import load_environment
from whatcouchquickstartexample.model import Session
from whatcouch.model import Database, User, Group, Permission
from couchdbkit.loaders import FileSystemDocsLoader

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup whatcouchquickstartexample here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Add design docs to CouchDB.
    loader = FileSystemDocsLoader(sys.path[0] + '/whatcouchquickstartexample/_design')
    loader.sync(Session.auth)

    # Add a user, group, and permission to CouchDB.
    user_name = 'admin'
    user_password = 'password'
    group_name = 'administrators'
    perm_name = 'superpowers'

    if User.find_by_username(user_name) is not None:
        raise Exception('User already exists.')
    if Group.find_by_name(group_name) is not None:
        raise Exception('Group already exists.')
    if Permission.find_by_name(perm_name) is not None:
        raise Exception('Permission already exists.')

    perm = Permission(name=perm_name)
    perm.save()
    group = Group(name=group_name)
    group.permissions.append(perm)
    group.save()
    user = User.create(user_name, user_password)
    user.groups.append(group)
    user.save()

