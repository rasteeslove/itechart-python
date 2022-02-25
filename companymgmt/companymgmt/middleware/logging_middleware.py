"""
This module is for the middleware which logs all client requests.

Sources:
https://wilspi.com/post/tech/django-middleware-to-log-requests/
"""

import socket
import time
import json
import logging


logging.basicConfig(filename='requests.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)03d %(name)s '
                           '%(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """
    A middleware for logging all request and response data into a file.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.log_data = {}

        self.log_data['remote_address'] = request.META['REMOTE_ADDR']
        self.log_data['server_hostname'] = socket.gethostname()
        self.log_data['request_method'] = request.method
        self.log_data['request_path'] = request.get_full_path()

        if request.body:
            request_body = request.body.decode('utf-8')
            self.log_data['request_body'] = request_body

        self.start_time = time.time()
        response = self.get_response(request)
        run_time = time.time() - self.start_time
        self.log_data['run_time'] = run_time

        if response:
            if response.get('content-type') == 'application/json':
                if getattr(response, 'streaming', False):
                    response_body = '[Streaming]'
                else:
                    response_body = response.content
            else:
                response_body = '[Not JSON]'
        else:
            response_body = None

        if response:
            self.log_data['response_status'] = response.status_code
        if response_body:
            self.log_data['response_body'] = response_body

        logger.info(msg=self.log_data)

        return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            logger.exception("Unhandled Exception: " + str(e))
        return exception
