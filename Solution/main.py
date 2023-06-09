class Company:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def set_customers(self, customers):
        self.customers = customers

    def get_customers(self):
        return self.customers


class Customer:
    def __init__(self, cust_id, name, email):
        self.cust_id = cust_id
        self.name = name
        self.email = email


class RegCustomer(Customer):
    def __init__(self, cust_id, name, email, dt_reg):
        super().__init__(cust_id, name, email)
        self.dt_reg = dt_reg
        self.membership = None

    def set_membership(self, membership):
        self.membership = membership

    def get_membership(self):
        return self.membership

    def get_dt_reg(self):
        return self.dt_reg


class Membership:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_discount(self):
        return self.discount


class GoldMembership(Membership):
    def __init__(self):
        super().__init__("GOLD", 20000.0, 10.0)


class PlatinumMembership(Membership):
    def __init__(self):
        super().__init__("PLATINUM", 30000.0, 15.0)


class MembershipFactory:
    __instance = None

    @staticmethod
    def get_instance():
        if MembershipFactory.__instance is None:
            MembershipFactory()
        return MembershipFactory.__instance

    def __init__(self):
        if MembershipFactory.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            MembershipFactory.__instance = self

    def create(self, membership_type):
        if membership_type == "GOLD":
            return GoldMembership()
        elif membership_type == "PLATINUM":
            return PlatinumMembership()
        else:
            return None


def display(company):
    customers = company.get_customers()
    for customer in customers:
        if isinstance(customer, RegCustomer):
            print("Customer Id : ", customer.cust_id)
            print("Customer Name : ", customer.name)
            print("Customer Email : ", customer.email)
            print("Membership Details : ", customer.get_membership().get_name())
            print("Date Reg : ", customer.get_dt_reg())
        else:
            print("Customer Id : ", customer.cust_id)
            print("Customer Name : ", customer.name)
            print("Customer Email : ", customer.email)
        print("===========================")


if __name__ == '__main__':
    # create a company
    c1 = Company("Amazon")

    # Create customers
    cus1 = Customer("1", "Shruthi", "shru133@gmail.com")
    cus2 = Customer("2", "Sreeja", "sreeja@gmail.com")

    # Create RegCustomer
    rc1 = RegCustomer("3", "Suraj", "suraj@gmail.com", "20-10-2020")
    rc2 = RegCustomer("4", "Sujay", "sujay@gmail.com", "15-5-2019")

    # Singleton Design Pattern - only one object will be created
    # MembershipFactory is created by call a method getInstance -
    # in which object instantiation is done using singleton pattern
    mem = MembershipFactory.get_instance()

    rc1.set_membership(mem.create("GOLD"))
    rc2.set_membership(mem.create("PLATINUM"))

    customers = [cus1, cus2, rc1, rc2]

    # Add customer and regCustomer to company
    c1.set_customers(customers)

    display(c1)