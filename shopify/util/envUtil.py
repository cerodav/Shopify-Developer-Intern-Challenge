import os

class EnvUtil:

    @staticmethod
    def getEnv(default='default'):
        env = os.getenv('APP_ENV', None)
        if env is None:
            os.environ['APP_ENV'] = default
        return os.getenv('APP_ENV')
