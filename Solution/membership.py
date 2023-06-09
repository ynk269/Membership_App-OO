class Membership:
    def __init__(self, type_of_membership, discount, fees):
        self.type_of_membership = type_of_membership
        self.discount = discount
        self.fees = fees

    def get_type_of_membership(self):
        return self.type_of_membership

    def set_type_of_membership(self, type_of_membership):
        self.type_of_membership = type_of_membership

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_fees(self):
        return self.fees

    def set_fees(self, fees):
        self.fees = fees

    def __str__(self):
        return f"Membership [typeOfMembership={self.type_of_membership}, discount={self.discount}, fees={self.fees}]"