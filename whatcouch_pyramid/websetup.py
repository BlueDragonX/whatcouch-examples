
import os, sys, pkg_resources
from paste.deploy.loadwsgi import appconfig
from whatcouch_pyramid.model import Session, init_model
from whatcouch.model import User, Group, Permission
from couchdbkit.loaders import FileSystemDocsLoader

def setup_app(config, settings):
    # Init CouchDB model.
    print "initializing model"
    init_model(config)

    # Add design docs to CouchDB.
    path = sys.path[0] + '/_design'
    print "loading views at %s" % path
    loader = FileSystemDocsLoader(path)
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

    print "loading data"
    perm = Permission(name=perm_name)
    perm.save()
    group = Group(name=group_name)
    group.permissions.append(perm)
    group.save()
    user = User.create(user_name, user_password)
    user.groups.append(group)
    user.save()

def main(argv=sys.argv):
    dist = pkg_resources.get_distribution('whatcouch_pyramid')
    root = dist.location
    config = 'config:' + os.path.join(root, 'development.ini')
    settings = appconfig(config, "whatcouch_pyramid")
    setup_app(config, settings)

if __name__ == '__main__':
    main()

