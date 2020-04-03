from dao.Entity import Entity

class VENDORS_Entity(Entity):

    def __init__(self):
        self.key_name = 'VEND_ID'
        self.table_name = 'vendors'
        self.atr_vend_country = None
        self.atr_vend_zip = None
        self.atr_vend_state = None
        self.atr_vend_city = None
        self.atr_vend_address = None
        self.atr_vend_name = None



