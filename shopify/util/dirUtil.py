import os
import pathlib

class DirUtil:

    @staticmethod
    def getCurrentScriptDirectory():
        return pathlib.Path(__file__).parent.absolute()

    @staticmethod
    def getParentDir(path):
        return pathlib.Path(path).parent.absolute()

    @staticmethod
    def makeDir(path):
        return os.mkdir(path)

    @staticmethod
    def isDir(path):
        return os.path.isdir(path)

    @staticmethod
    def getShopifyDir():
        curentScriptDir = DirUtil.getCurrentScriptDirectory()
        projectDir = DirUtil.getParentDir(curentScriptDir)
        return projectDir

    @staticmethod
    def getWebDir():
        curentScriptDir = DirUtil.getCurrentScriptDirectory()
        projectDir = DirUtil.getParentDir(curentScriptDir)
        return os.path.join(projectDir, 'web')

    @staticmethod
    def getFakeDataDir(tableName='inventory'):
        curentScriptDir = DirUtil.getCurrentScriptDirectory()
        projectDir = DirUtil.getParentDir(curentScriptDir)
        fakedataDir = os.path.join(projectDir, 'resource', 'fakedata')
        return os.path.join(fakedataDir, '{}.json'.format(tableName))


if __name__ == '__main__':
    p = DirUtil.getCurrentScriptDirectory()
    print(p)
    print(DirUtil.getParentDir(p))
