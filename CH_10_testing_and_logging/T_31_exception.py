import logging

logging.basicConfig()
logger = logging.getLogger()

try:
    raise RuntimeError('some runtime error')
except Exception as exception:
    logger.exception('Got an exception: %s', exception)

logger.error('And an error')

