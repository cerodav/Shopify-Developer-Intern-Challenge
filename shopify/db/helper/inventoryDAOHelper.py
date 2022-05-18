from datetime import datetime
from shopify.db.model.core import InventoryTableEntry, UndeleteTableEntry
from shopify.db.session.inventoryTable import InventoryTable
from shopify.db.session.undeleteTable import UndeleteTable
from shopify.db.session.sessionFactory import DefaultSessionFactory
from shopify.util.validatorUtil import ValidatorUtil

class InventoryTableDA0Helper:

    session = DefaultSessionFactory().getSession()
    inventoryTable = session.getTable(InventoryTable.tableName)
    undeleteTable = session.getTable(UndeleteTable.tableName)

    @staticmethod
    def setTimeVars(item):
        t = datetime.now()
        item.setCreatedTime(t)

    @staticmethod
    def getAll():
        res = list(InventoryTableDA0Helper.inventoryTable.table.items())
        return res

    @staticmethod
    def delete(code, comment=None):
        if code in InventoryTableDA0Helper.inventoryTable.table:
            i = InventoryTableDA0Helper.inventoryTable.get(code)
            d = UndeleteTableEntry(inventoryTableEntry=i, comment=comment)
            InventoryTableDA0Helper.undeleteTable.create(d)
            InventoryTableDA0Helper.inventoryTable.delete(code)
        else:
            raise Exception('Product code does not exist')

    @staticmethod
    def validateArgs(args):
        validationMapper = {
            'name': ValidatorUtil.isValidString,
            'code': ValidatorUtil.isValidCode,
            'type': ValidatorUtil.isValidString,
            'supplier': ValidatorUtil.isValidString,
            'quantity': ValidatorUtil.isValidInt,
            'price': ValidatorUtil.isValidFloat,
        }
        isValid = True
        for key in args:
            val = args[key]
            if key in validationMapper:
                isValid &= validationMapper[key](val)
        return isValid

    @staticmethod
    def create(inventoryId=None, name=None, code=None,
               type=None, supplier=None, quantity=None, price=None):
        args = {
            'inventoryId': inventoryId, 'name': name, 'code': code,
            'type': type, 'supplier': supplier, 'quantity': quantity, 'price': price
        }

        if not InventoryTableDA0Helper.validateArgs(args):
            raise Exception('Invalid arguments passed. Returning ...')

        i = InventoryTableEntry()
        for key in args:
            if args[key] is not None:
                setattr(i, key, args[key])
        InventoryTableDA0Helper.setTimeVars(i)
        InventoryTableDA0Helper.inventoryTable.create(i)

    @staticmethod
    def update(inventoryId=None, name=None, code=None,
               type=None, supplier=None, quantity=None, price=None):
        args = {
            'inventoryId': inventoryId, 'name': name, 'code': code,
            'type': type, 'supplier': supplier, 'quantity': quantity, 'price': price
        }

        if not InventoryTableDA0Helper.validateArgs(args):
            raise Exception('Invalid arguments passed. Returning ...')

        if code in InventoryTableDA0Helper.inventoryTable.table:
            i = InventoryTableDA0Helper.inventoryTable.get(code)
            for key in args:
                if args[key] is not None:
                    setattr(i, key, args[key])
            InventoryTableDA0Helper.inventoryTable.update(code, i)
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
            op.append({col: getattr(item[1], col) for col in InventoryTable.columns})
        return op



