
##################################################################


import logging

logger = logging.getLogger()
logger.error('simple error', extra=dict(some_variable='my value'))

##################################################################


import logging

logging.basicConfig(format='%(some_variable)s: %(message)s')
logger = logging.getLogger()
logger.error('the message', extra=dict(some_variable='my value'))
