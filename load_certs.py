import xmlrpclib
import sys, os

server = xmlrpclib.ServerProxy('https://api.webfaction.com/')
session_id, account = server.login(os.environ['WEBFACTION_USER'], os.environ['WEBFACTION_PASS'], "Web585", 2)

cert_name = sys.argv[1]     # name of cert in webfaction
cert_folder = sys.argv[2]   # path to cert folder

with open(os.path.join( cert_folder, cert_name + ".cer"), 'r') as f:
    cert = f.read()
with open(os.path.join( cert_folder, cert_name + ".key"), 'r') as f:
    key = f.read()
with open(os.path.join( cert_folder, "ca.cer"), 'r') as f:
    ca_cert = f.read()

clean_cert_name = cert_name.replace(".","_")
try:
    server.create_certificate(session_id, clean_cert_name, cert, key, ca_cert)
    print("New certificate created")
except xmlrpclib.Fault as e:
    if 'Ssl certificate with this Name and Account already exists.' in e.faultString:
        try:
            server.update_certificate(session_id, clean_cert_name, cert, key, ca_cert)
            print("Updated certificate")
        except xmlrpclib.Fault as e:
            print('Error connecting to Webfaction API. Error: {}'.format(e))
    else:
        print('Error connecting to Webfaction API. Error: {}'.format(e))
