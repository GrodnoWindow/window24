from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.authentication import CSRFCheck
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def enforce_csrf(request):
    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)


class JWTAuthenticationApp(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        enforce_csrf(request)
        user = self.get_user(validated_token)
        return (user, None)

# import jwt
# import datetime
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from rest_framework import exceptions
# from rest_framework.authentication import BaseAuthentication
#
#
# def generate_access_token(user):
#     payload = {
#         'user_id': user.id,
#         'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         'iat': datetime.datetime.utcnow()
#     }
#
#     return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
#
#
# class JWTAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         token = request.COOKIES.get('jwt')
#
#         if not token:
#             return None
#
#         try:
#             payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise exceptions.AuthenticationFailed('unauthenticated')
#
#         user = get_user_model().objects.filter(id=payload['user_id']).first()
#
#         if user is None:
#             raise exceptions.AuthenticationFailed('User not found!')
#
#         return (user, None)
