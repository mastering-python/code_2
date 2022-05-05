import logging


def get_handlers(logger):
    handlers = []
    # Walk through the loggers and their parents recursively to
    # fetch the handlers
    while logger:
        handlers += logger.handlers

        if logger.propagate:
            logger = logger.parent
        else:
            break

    # Python has a lastResort handler in case no handlers are
    # defined
    if not handlers and logging.lastResort:
        handlers.append(logging.lastResort)

    return handlers


def debug_loggers():
    logger: logging.Logger
    for name, logger in logging.root.manager.loggerDict.items():
        # Placeholders are loggers without settings
        if isinstance(logger, logging.PlaceHolder):
            print('skipping', name)
            continue

        level = logging.getLevelName(logger.getEffectiveLevel())
        handlers = get_handlers(logger)
        print(f'{name}@{level}: {handlers}')


if __name__ == '__main__':
    a = logging.getLogger('a')
    a.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    ab = logging.getLogger('a.b')
    ab.setLevel(logging.DEBUG)
    ab.addHandler(handler)

    debug_loggers()
