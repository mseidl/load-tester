import xmlrpclib
import logging
from config import *

def xmlrpc_call(errors, mutex):
    """Make xmlrpc calls to generate load"""

    try:
        # Login
        client = xmlrpclib.Server(url, verbose=0)
        key = client.auth.login(user, password)

        #client.channel.listAllChannels(key)
        client.activationkey.create(key, "", "description", "", [], False)
        xmlcall_log.INFO('called a function')
    except xmlrpclib.Fault, err:
        logging.error('Error #%d: %s' % (err.faultCode, error.faultString))
    except socket.error, err:
        with mutex:
            errors.inc()
        logging.error('Error #%d: %s' % (err.faultCode, err.faultString))
    finally:
        client.auth.logout(key)
