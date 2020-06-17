from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class ErrorCodeWithMessage:
    def __init__(self, code, message):
        self.code = code
        self.message = message


class ERROR_CODES:
    def __init__(self):
        pass

    # Auth Errors
    GENERAL_ERROR = ErrorCodeWithMessage('GENERAL_ERROR', _('A general error has occurred'))
    WRONG_CREDENTIALS = ErrorCodeWithMessage('WRONG_CREDENTIALS', _('Invalid credentials were provided'))
    NOT_FOUND = ErrorCodeWithMessage('NOT_FOUND', _('The resource was not found'))
    INTERNAL_SERVER_ERROR = ErrorCodeWithMessage('INTERNAL_SERVER_ERROR', _('Internal server error'))
    REGISTRATION_TIMEOUT = ErrorCodeWithMessage('REGISTRATION_TIMEOUT', _('User registration timed out'))
    TRANSLATION_IMPROPERLY_CONFIGURED = ErrorCodeWithMessage('INVALID_TRANSLATION_CONFIG', _('Translation was improperly configured'))
    TRANSLATION_NOT_FOUND = ErrorCodeWithMessage('TRANSLATION_NOT_FOUND', _('Translation was not found'))
    INVALID_FILE_TYPE = ErrorCodeWithMessage('INVALID_FILE_TYPE', _('File type is invalid or missing'))
    BAD_REQUEST = ErrorCodeWithMessage('BAD_REQUEST', _('Bad request'))

    @staticmethod
    def error_by_code(code: str):
        for k, v in ERROR_CODES.__dict__.items():
            if isinstance(v, ErrorCodeWithMessage) and v.code == code:
                return v
        return None


class ServerExceptionWithCode(APIException):
    status_code = 500

    def __init__(self, error_code: ErrorCodeWithMessage = None, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        if error_code is None:
            self.error_code = self.default_code

        self.code = error_code.code
        self.detail = error_code.message
        self.status_code = status_code

