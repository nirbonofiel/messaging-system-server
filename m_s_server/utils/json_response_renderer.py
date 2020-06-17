from rest_framework import status
from rest_framework.renderers import JSONRenderer

from m_s_server import settings
from m_s_server.utils.server_errors import ERROR_CODES


class JsonResponseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if status.is_client_error(renderer_context['response'].status_code) or \
                status.is_server_error(renderer_context['response'].status_code):

            if isinstance(data, dict) and 'detail' in data and 'code' in data:
                message = data['detail']
                code = data['code']
            elif isinstance(data, dict) and 'detail' in data:
                message = data['detail']
                code = ERROR_CODES.GENERAL_ERROR.code
            elif isinstance(data, dict):
                message = data
                code = ERROR_CODES.GENERAL_ERROR.code
            else:
                message = str(data)
                code = ERROR_CODES.GENERAL_ERROR.code

            if not settings.DEBUG:
                error = ERROR_CODES.error_by_code(code)
                if error:
                    message = error.message
                else:
                    message = ERROR_CODES.GENERAL_ERROR.message

            response_data = {'success': False, 'data': None, 'error': {'message': message, 'code': code}}
        else:
            response_data = {'success': True, 'data': data, 'error': None}
        return super(JsonResponseRenderer, self).render(response_data, accepted_media_type, renderer_context)
