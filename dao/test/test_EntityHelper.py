from dao.EntityHelper import EnityHelper
from dao.entities.CUSTOMERS import CUSTOMERS_Entity
from dao.entities.VENDORS import VENDORS_Entity


customer = CUSTOMERS_Entity()
customer.key_value = 'new'
customer.atr_cust_name  = 'new cust '

EnityHelper.insert(customer)


vendor = VENDORS_Entity()
vendor.key_value = 'new'
vendor.atr_vend_name = 'new'

EnityHelper.insert(vendor)



EnityHelper.delete(customer)
EnityHelper.delete(vendor)