#!/usr/bin/python

import xmlrpclib
import sys, os

command = sys.argv[1]
server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
session_id, account = server.login(os.environ['WEBFACTION_USER'], os.environ['WEBFACTION_PASS'])

# https://docs.webfaction.com/xmlrpc-api/apps.html
if command == "create":
    app_name = raw_input('Enter app name: ')
    database_password = raw_input('Enter database password: ')
    server.create_app(session_id, app_name, 'mod_wsgi-4.5.15_python-3.5', False, '', False)
    server.create_db(session_id, '{}_db'.format(app_name), 'postgresql', database_password)

elif command == "delete":
    app_name = raw_input('Enter app name: ')
    server.delete_app(session_id, app_name)
    server.delete_db(session_id, '{}_db'.format(app_name), 'postgresql')
    server.delete_db_user(session_id, '{}_db'.format(app_name), 'postgresql')

elif command == "status":
    app_list = server.list_apps(session_id)
    print 'Apps:'
    for app in app_list:
        print '\t{}: {}'.format(app['name'], app['type'])

    db_list = server.list_dbs(session_id)
    print 'DBs:'
    for db in db_list:
        print '\t{}'.format(db['name'])

    db_users_list = server.list_db_users(session_id)
    print 'DB Users:'
    for user in db_users_list:
        print '\t{}'.format(user['username'])

elif command == "get_certs":
    certs = server.list_certificates(session_id)
    for cert in certs:
        print cert["name"]

elif command == "get_certs_files":
    certs = server.list_certificates(session_id)
    cert_name = sys.argv[2]
    cert_path = sys.argv[3]
    cert = [cert for cert in certs if cert['name'] == cert_name][0]
    with open(os.path.join( cert_path, cert_name + ".cert"), 'w') as f:
        f.write(cert['certificate'])
    with open(os.path.join( cert_path, cert_name + ".key"), 'w') as f:
        f.write(cert['private_key'])
    with open(os.path.join( cert_path, "ca.cert"), 'w') as f:
        f.write(cert['intermediates'])
