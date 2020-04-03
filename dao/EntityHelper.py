import inspect
# from dao.Entity import Entity
from dao.OracleDb import OracleDb


class EnityHelper:

    def getAttributes(entity):

        attributes = inspect.getmembers(entity, lambda a: not (inspect.isroutine(a)))

        table_attributes = []
        table_values = []

        for attribute in attributes:
            if (attribute[0].startswith('atr')):
                print(attribute[0].replace('atr_', ''))
                print(attribute[1])

                table_attributes.append(attribute[0].replace('atr_', ''))

                if isinstance(attribute[1], str):
                    table_values.append("'" + attribute[1] + "'")
                elif attribute[1] is None:
                    table_values.append('null')
                else:
                    table_values.append(str(attribute[1]))

        return (',').join(table_attributes), (',').join(table_values)


    def insert(entity, autoincrement=False):
        # TODO chaeck if entity is Entity instance

        db = OracleDb()
        attributes, values = EnityHelper.getAttributes(entity)

        if not autoincrement:
            attributes+=','+entity.key_name

            if isinstance(entity.key_value, str):
                key_value = "'" + entity.key_value + "'"
            else:
                key_value = entity.key_value
            values+= ',' + key_value

        query = "insert into {0} ({1}) values ({2})".format(entity.table_name, attributes, values)

        print(query)

        db.execute(query)



    def delete(entity):
        # TODO chaeck if entity is Entity instance

        db = OracleDb()

        if isinstance(entity.key_value,str):
            key_value="'"+entity.key_value+"'"
        else:
            key_value =entity.key_value

        query = """DELETE FROM {0} WHERE {1} = {2}""".format(entity.table_name, entity.key_name, key_value)

        # print(query)

        db.execute(query)




# if __name__=="__main__":
#     entity = Entity
#     EnityHelper.insert(entity)
#     EnityHelper.delete(entity)
