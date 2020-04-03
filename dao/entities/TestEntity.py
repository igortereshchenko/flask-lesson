from dao.Entity import Entity
from dao.EntityHelper import EnityHelper

class Customer(Entity):

    def __init__(self):

        self.atr_CUST_NAME = 'bob'
        self.key_name='CUST_ID'
        self.key_value = 'bob'
        self.table_name='CUSTOMERS'



if __name__=="__main__":

    customer = Customer()

    EnityHelper.insert(customer)


