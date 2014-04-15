import logging

logger = logging.getLogger(__name__)


class HttpRequestLogMiddleware(object):
    def process_request(self, request):
        logger.debug(request)