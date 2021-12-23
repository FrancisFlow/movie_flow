from logging import DEBUG


class Config:

    """
    Parent configuration class
    """

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