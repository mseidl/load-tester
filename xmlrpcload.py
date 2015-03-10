import xmlrpclib
import logging

logfile = 'xmlrpc.log'
logging.basicConfig(filename = logfile, level = logging.DEBUG)

def xmlrpc_call():
    # Config for xmlrpc
    url = 'url'
    user = 'user'
    password = 'password'

    client = xmlrpclib.Server(url, verbose=0)
    key = client.auth.login(user, password)
    try:
        client.channel.listAllChannels(key)
        print "Got list ok"
    except xmlrpclib.Fault, err:
        logging.error('Error #%d: %s' % (err.faultCode, error.faultString))
