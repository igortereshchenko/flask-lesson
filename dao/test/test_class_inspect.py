import inspect
class TestClass:

    atr_a = 1;

    atr_b ='1';


instance = TestClass()
attributes = inspect.getmembers(instance,lambda a:not(inspect.isroutine(a)))

table_attributes = []
table_values = []



for attribute in attributes:
    if (attribute[0].startswith('atr')):
        print(attribute[0].replace('atr_',''))
        print(attribute[1])

        table_attributes.append(attribute[0].replace('atr_',''))

        if isinstance(attribute[1],str):
            table_values.append('"'+attribute[1]+'"')
        else:
            table_values.append(str(attribute[1]))


print((',').join(table_attributes))
print((',').join(table_values))