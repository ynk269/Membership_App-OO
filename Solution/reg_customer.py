from .customer import Customer

class RegCustomer(Customer):
    def __init__(self, custId, name, email, dtReg=None):
        super().__init__(custId, name, email)
        self.dtReg = dtReg
        self.membership = None

    def getDtReg(self):
        return self.dtReg

    def setDtReg(self, dtReg):
        self.dtReg = dtReg

    def getMembership(self):
        return self.membership

    def setMembership(self, membership):
        self.membership = membership