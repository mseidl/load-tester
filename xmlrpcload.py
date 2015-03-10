import xmlrpclib
import logging

# Config for xmlrpc
url = 'enter url'
user = 'user'
password = 'password'

logfile = 'xmlrpc.log'
logging.basicConfig(filename = logfile, level = logging.DEBUG)

client = xmlrpclib.Server(url, verbose=0)
key = client.auth.login(user, password)

try:
    client.channel.listAllChannels(key)
except xmlrpclib.Fault, err:
    logging.error('Error #%d: %s' % (err.faultcode, error.faultString))
