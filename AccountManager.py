from ZODB import FileStorage, DB, PersistentMapping
import transaction
from Account import *
import json

storage = FileStorage.FileStorage('db/mydatabase.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

class AccountManager:
    def __init__(self):
        self.accounts = self.initAccount()

    def initAccount(self):
        if "accounts" not in root:
            root["accounts"] = {}
        return root["accounts"]

    def updateDB(self):
        root["accounts"] = self.accounts
        transaction.commit()

    def addAccount(self, name):
        if name in self.accounts:
            return "Already exists"

        self.accounts[name] = Account(name)
        self.updateDB()
        return "Added successfully"

    def listAccounts(self):
        return [acc.toJson() for acc in self.accounts.values()]