import xmlrpclib
import logging
from config import *

logfile = 'xmlrpc.log'
logging.basicConfig(filename = logfile, level = logging.DEBUG)

def xmlrpc_call(errors):
    """Make xmlrpc calls to generate load"""

    client = xmlrpclib.Server(url, verbose=0)
    key = client.auth.login(user, password)
    try:
        #client.channel.listAllChannels(key)
        client.activationkey.create(key, "", "description", "", [], False)
        print "Got list ok"
    except xmlrpclib.Fault, err:
        errors += 1
        print err
        logging.error('Error #%d: %s' % (err.faultCode, error.faultString))
