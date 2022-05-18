from shopify.db.session.inventoryTable import InventoryTable
from shopify.db.session.undeleteTable import UndeleteTable
from shopify.db.session.sessionFactory import DefaultSessionFactory

class UndeleteDAOHelper:

    session = DefaultSessionFactory().getSession()
    inventoryTable = session.getTable(InventoryTable.tableName)
    undeleteTable = session.getTable(UndeleteTable.tableName)

    @staticmethod
    def getAll():
        res = list(UndeleteDAOHelper.undeleteTable.table.items())
        return res

    @staticmethod
    def undelete(code):
        if code in UndeleteDAOHelper.undeleteTable.table:
            i = UndeleteDAOHelper.undeleteTable.get(code)
            UndeleteDAOHelper.inventoryTable.create(i.inventoryTableEntry)
            UndeleteDAOHelper.undeleteTable.delete(code)
        else:
            raise Exception('Product code does not exist')

    @staticmethod
    def rollback():
        pass

    @staticmethod
    def toDict(listOfItems):
        op = []
        if not isinstance(listOfItems, list):
            listOfItems = [listOfItems]
        for item in listOfItems:
            op.append({col: getattr(item[1], col) for col in UndeleteTable.columns})
        return op



