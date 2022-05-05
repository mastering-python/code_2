import logging


logger = logging.getLogger(__name__)


class MyClass(object):

    def __init__(self, count):
        self.logger = logger.getChild(self.__class__.__name__)

##################################################################


import logging

logger = logging.getLogger('main_module.sub_module')
logger.addHandler(logging.FileHandler('sub_module.log'))

##################################################################


import logging

logger = logging.getLogger('main_module.sub_module')
logger.setLevel(logging.DEBUG)

##################################################################


import logging

logger = logging.getLogger()
exception = 'Oops...'
logger.error('Some horrible error: %r', exception)
