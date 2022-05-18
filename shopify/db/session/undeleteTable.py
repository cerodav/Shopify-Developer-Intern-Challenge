class UndeleteTable:
    tableName = 'Undelete'
    columns = ['code', 'comment']

    def __init__(self, session):
        self.table = None
        self.session = session

    def create(self, undeleteTableEntry):
        self.table[undeleteTableEntry.code] = undeleteTableEntry
        self.session.get(UndeleteTable.tableName)[undeleteTableEntry.code] = undeleteTableEntry

    def read(self, index=None):
        if index == None:
            return self.table
        else:
            return self.table.get(index, None)

    def delete(self, code):
        del self.table[code]
        del self.session.get(UndeleteTable.tableName)[code]

    def get(self, code):
        return self.table[code]

    @staticmethod
    def bootstrap(session):
        i = UndeleteTable(session)
        i.table = dict()

        if UndeleteTable.tableName in session:
            dbTable = session.get(UndeleteTable.tableName)
            for key in dbTable:
                i.table[key] = dbTable[key]
        else:
            session[UndeleteTable.tableName] = {}
        return i

    def addFakeData(self):
        pass









