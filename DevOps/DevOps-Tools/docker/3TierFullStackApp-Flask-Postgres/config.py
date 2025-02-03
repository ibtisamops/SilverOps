import os
import secrets

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://ibtisam:ibtisam@db/loveyou_ibtisam'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)  # Generate a new secret key each time the app runs


