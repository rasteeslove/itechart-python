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
                    format='%(asctime)s,%(msecs)03d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LoggingMiddleware:
    """
    A middleware for logging all "*/api/*" requests into a file.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.start_time = time.time() # timing the execution
        self.log_data = {
            "remote_address": request.META["REMOTE_ADDR"],
            "server_hostname": socket.gethostname(),
            "request_method": request.method,
            "request_path": request.get_full_path(),
        }

        # Only logging "*/api/*" patterns
        if "/api/" in str(request.get_full_path()):
            req_body = (json.loads(request.body.decode("utf-8"))
                            if request.body else {})
            self.log_data["request_body"] = req_body

        response = self.get_response(request)

        if response and response["content-type"] == "application/json":
            response_body = json.loads(response.content.decode("utf-8"))
            self.log_data["response_body"] = response_body
        self.log_data["run_time"] = time.time() - self.start_time

        logger.info(msg=self.log_data)

        return response

    def process_exception(self, request, exception):
        try:
            raise exception
        except Exception as e:
            logger.exception("Unhandled Exception: " + str(e))
        return exception
