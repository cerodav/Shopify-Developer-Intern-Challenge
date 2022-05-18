import json
from shopify.util.dirUtil import DirUtil
from shopify.db.model.core import InventoryTableEntry

class InventoryTable:

    tableName = 'Inventory'
    columns = ['inventoryId', 'name', 'code', 'type', 'supplier', 'quantity', 'price', 'createdTime']

    def __init__(self, session):
        self.table = None
        self.counter = None
        self.session = session

    def create(self, inventoryTableEntry):
        self.counter += 1
        inventoryTableEntry.inventoryId = self.counter
        self.table[inventoryTableEntry.code] = inventoryTableEntry
        self.session.get(InventoryTable.tableName)[inventoryTableEntry.code] = inventoryTableEntry

    def read(self, index=None):
        if index == None:
            return self.table
        else:
            return self.table.get(index, None)

    def update(self, code, inventoryTableEntry):
        self.table[code] = inventoryTableEntry
        self.session.get(InventoryTable.tableName)[code] = inventoryTableEntry

    def delete(self, code):
        del self.table[code]
        del self.session.get(InventoryTable.tableName)[code]

    def get(self, code):
        return self.table[code]

    @staticmethod
    def bootstrap(session):
        i = InventoryTable(session)
        i.counter = 0
        i.table = dict()

        if InventoryTable.tableName in session:
            dbTable = session.get(InventoryTable.tableName)
            for key in dbTable:
                i.counter += 1
                i.table[key] = dbTable[key]
        else:
            session[InventoryTable.tableName] = {}
        return i

    def addFakeData(self):
        path = DirUtil.getFakeDataDir(tableName=InventoryTable.tableName)
        data = json.loads(open(path, 'r').read())
        for row in data:
            r = InventoryTableEntry()
            r.type = row.get('type')
            r.name = row.get('name')
            r.code = row.get('code')
            r.quantity = row.get('quantity')
            r.supplier = row.get('supplier')
            r.createdTime = row.get('createdTime')
            r.price = row.get('price')
            self.create(r)




        



