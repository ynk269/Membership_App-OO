class Customer:
    def __init__(self, custId, name, email):
        self.custId = custId
        self.name = name
        self.email = email

    def getCustId(self):
        return self.custId

    def setCustId(self, custId):
        self.custId = custId

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email