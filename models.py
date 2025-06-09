from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from authlib.oauth2.rfc6749.models import ClientMixin, TokenMixin

Base = declarative_base()

class OAuth2Client(Base, ClientMixin):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    client_id = Column(String(48), unique=True, nullable=False)
    client_secret = Column(String(120), nullable=False)
    redirect_uris = Column(String(255), nullable=False)
    scope = Column(String(255), default='')

class OAuth2Token(Base, TokenMixin):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    client_id = Column(String(48))
    user_id = Column(Integer)
    access_token = Column(String(255), unique=True)
    refresh_token = Column(String(255), unique=True)
    scope = Column(String(255))
    expires_at = Column(Integer)

    def get_scope(self):
        return self.scope

    def get_expires_at(self):
        return self.expires_at
