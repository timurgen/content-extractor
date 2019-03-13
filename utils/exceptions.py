"""
Custom exception handling module
"""
from flask import jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


class JSONExceptionHandler(object):
    """
    Custom exception handler that outputs known exception as JSON entities
    """

    def __init__(self, app=None):
        self.app = None
        if app:
            self.init_app(app)

    @staticmethod
    def std_handler(error):
        """
        Custom exception handler
        :param error: exception that occured
        :return: JSON response
        """
        response = jsonify(message=str(error))
        response.status_code = error.code if isinstance(error, HTTPException) else 500
        return response

    def init_app(self, app):
        """
        Init method that register all default exception to ba handled by this handler
        :param app:
        :return:
        """
        self.app = app
        self.register(HTTPException)
        for code, _ in default_exceptions.items():
            self.register(code)

    def register(self, exception_or_code, handler=None):
        """
        Function to add exceptions to custom error handler
        :param exception_or_code:
        :param handler: custom handler or "standard" custom handler if not assigned
        :return:
        """
        self.app.errorhandler(exception_or_code)(handler or self.std_handler)
