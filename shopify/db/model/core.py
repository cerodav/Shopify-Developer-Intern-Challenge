class InventoryTableEntry:

    def __init__(self, inventoryId=None, name=None, code=None, type=None, supplier=None, quantity=None, price=None, createdTime=None):
        self.inventoryId = inventoryId
        self.name = name
        self.code = code
        self.type = type
        self.supplier = supplier
        self.quantity = quantity
        self.price = price
        self.createdTime = createdTime

    def setCreatedTime(self, ct):
        self.createdTime = ct

    def setName(self, name):
        self.name = name

    def setCode(self, code):
        self.code = code

    def setType(self, type):
        self.type = type

    def setSupplier(self, supplier):
        self.supplier = supplier

    def setQuantity(self, qty):
        self.quantity = qty

    def setPrice(self, price):
        self.price = price



class UndeleteTableEntry:

    def __init__(self, inventoryTableEntry=None, comment=None):
        self.inventoryTableEntry = inventoryTableEntry
        self.comment = comment
        self.code = inventoryTableEntry.code
