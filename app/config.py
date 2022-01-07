from logging import DEBUG


class Config:

    """
    Parent configuration class
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

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