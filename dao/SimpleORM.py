
from dao.OracleDb import OracleDb
import os


class SimpleORM:


    def create_entity(table_name, table_owner):

        db = OracleDb()

        query = """
        SELECT
            trim(col.column_name),
            col.data_type,
            col.nullable
        FROM
            sys.all_tab_columns col
            INNER JOIN sys.all_tables t 
            ON col.owner = t.owner AND col.table_name = t.table_name
        WHERE
            col.owner = upper('{0}')
            AND col.table_name = '{1}'
        """.format(table_owner, table_name)

        result = db.execute(query)


        class_fields = ""


        # TODO modofy primary key extraction

        key_name =''
        for column_name, data_type, nullable in result.fetchall():
            if (column_name.endswith('_ID')):
                key_name = "'"+column_name+"'"
            else:
                class_fields += "        self.{0} = None\n".format('atr_'+column_name.lower())

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        with open(ROOT_DIR+"/file_templates/class_template.tml", "r") as file:
            class_file = file.read()
            class_file = class_file.replace('$ATTRIBUTES$', class_fields)
            class_file = class_file.replace('$CLASS_NAME$', table_name.upper())
            class_file = class_file.replace('$TABLE_NAME$', "'"+table_name.lower()+"'")


            class_file = class_file.replace('$KEY_NAME$', key_name)

            file.close()



            with open(ROOT_DIR+"/entities/{}.py".format(table_name.upper()), "w") as file:
                file.write(class_file)
                file.close()

