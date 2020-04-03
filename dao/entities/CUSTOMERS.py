from dao.Entity import Entity

class CUSTOMERS_Entity(Entity):

    def __init__(self):
        self.key_name = 'CUST_ID'
        self.table_name = 'customers'
        self.atr_cust_email = None
        self.atr_cust_contact = None
        self.atr_cust_country = None
        self.atr_cust_zip = None
        self.atr_cust_state = None
        self.atr_cust_city = None
        self.atr_cust_address = None
        self.atr_cust_name = None



