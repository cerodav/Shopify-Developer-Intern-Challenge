import os
import yaml
from shopify.util.dirUtil import DirUtil
from shopify.util.envUtil import EnvUtil

class ConfigUtil:

    def __init__(self, config=None, configFilePath=None):
        self.config = config
        self.configFilePath = configFilePath
        self.setup()

    def setup(self):
        if self.config is None:
            if self.configFilePath is None:
                self.configFilePath = ConfigUtil.getDefaultConfigFilePath()
            self.loadConfig()

    def loadConfig(self):
        file = open(self.configFilePath)
        self.config = yaml.full_load(file)

    def getConfig(self, key):
        res = self.config
        if res is not None and key in res:
            return res.get(key)

    def getServicePort(self):
        return int(self.getConfig('servicePort'))

    def isMockDB(self):
        return self.getConfig('mockDB')

    def isAugmentData(self):
        return self.getConfig('augmentData')

    def getLogDirPath(self):
        if self.getConfig('logPath') is None:
            curentScriptDir = DirUtil.getCurrentScriptDirectory()
            projectDir = DirUtil.getParentDir(curentScriptDir)
            return os.path.join(projectDir, 'logs')
        else:
            return self.getConfig('logPath')

    @staticmethod
    def getDefaultConfigFilePath():
        env = EnvUtil.getEnv()
        configFilePath = os.getenv('SHOPIFY_CONFIG_PATH', None)
        if configFilePath is None:
            curentScriptDir = DirUtil.getCurrentScriptDirectory()
            projectDir = DirUtil.getParentDir(curentScriptDir)
            configFilePath = os.path.join(projectDir, 'resource', 'config', 'settings_{}.yaml'.format(env))
        else:
            configFilePath = os.path(configFilePath)
        return configFilePath

if __name__ == '__main__':
    c = ConfigUtil()
    print(c.getConfig('database'))
