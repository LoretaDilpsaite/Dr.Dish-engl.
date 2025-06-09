from authlib.oauth2.rfc6749 import grants

class AuthorizationCodeGrant(grants.AuthorizationCodeGrant):
    def authenticate_user(self, code):
        return {'id': 1}  # mock user for testing
