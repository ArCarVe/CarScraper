import os


class Config(object):
    
    API_HOST = os.environ.get('API_HOST') or 'http://localhost:8080'
