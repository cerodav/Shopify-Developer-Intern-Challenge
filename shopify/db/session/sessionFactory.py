from replit import db
from collections import defaultdict
from shopify.db.session.inventoryTable import InventoryTable
from shopify.db.session.undeleteTable import UndeleteTable
from shopify.util.singletonType import SingletonType
from shopify.util.configUtil import ConfigUtil

class DefaultSessionFactory(metaclass=SingletonType):

    tableTypes = [InventoryTable, UndeleteTable]

    def __init__(self):
        if ConfigUtil().isMockDB():
            self.session = defaultdict()
        else:
            self.session = db
        self.tables = dict()
        self.setup()

    def getSession(self):
        return self

    def setup(self):
        for tableType in DefaultSessionFactory.tableTypes:
            self.tables[tableType.tableName] = tableType.bootstrap(self.session)

        if ConfigUtil().isAugmentData():
            for tableType in DefaultSessionFactory.tableTypes:
                self.tables[tableType.tableName].addFakeData()

    def getTable(self, tableName):
        if tableName in self.tables:
            return self.tables[tableName]


if __name__ == '__main__':
    d = DefaultSessionFactory()
    s = d.getSession()







