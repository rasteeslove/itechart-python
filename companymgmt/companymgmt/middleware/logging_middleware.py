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

        # log some essential request metadata:
        self.log_data['remote_address'] = request.META['REMOTE_ADDR']
        self.log_data['server_hostname'] = socket.gethostname()
        self.log_data['request_method'] = request.method
        self.log_data['request_path'] = request.get_full_path()

        # log the query params for GET requests:
        if request.GET:
            get = request.GET
            self.log_data['get_request'] = get

        # log the request body as a json-parsed dict:
        if request.body:
            body = json.loads(request.body)
            self.log_data['request_body'] = body

        # get response and log the run time:
        self.start_time = time.time()
        response = self.get_response(request)
        run_time = time.time() - self.start_time
        self.log_data['run_time'] = run_time

        logger.info(msg=self.log_data)

        return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            logger.exception("Unhandled Exception: " + str(e))
        return exception
