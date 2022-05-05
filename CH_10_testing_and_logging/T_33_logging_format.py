import logging


class FormattingMessage:

    def __init__(self, message, kwargs):
        self.message = message
        self.kwargs = kwargs

    def __str__(self):
        return self.message.format(**self.kwargs)


class FormattingAdapter(logging.LoggerAdapter):

    def process(self, msg, kwargs):
        msg, kwargs = super().process(msg, kwargs)
        return FormattingMessage(msg, kwargs), dict()


logger = FormattingAdapter(logging.root, dict())
logger.error('Hi {name}', name='Rick')

