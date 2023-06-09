class Company:
    def __init__(self, name):
        self.name = name
        self.customers = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_customers(self):
        return self.customers
    
    def set_customers(self, customers):
        self.customers = customers