from logging import DEBUG
import os

class Config:

    """
    Parent configuration class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class DevConfig(Config):
    """
    Child class of configuration
    """
    DEBUG=True

class ProdConfig(Config):
    """
    Child class for production configurations
    """
    pass

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}