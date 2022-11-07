import sqlite3


class Database:
    def __init__(self, path: str = 'shop_database.db'):
        self.db_path = path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = '''
        CREATE TABLE Users(
        id int NOT NULL,
        phone text
        )
        '''
        self.execute(sql, commit=True)

    def create_table_products(self):
        sql = '''
        CREATE TABLE Products(
        id int NOT NULL,
        name text NOT NULL,
        prise real,
        numbers integer,
        photo_path text
        )
        '''
        self.execute(sql, commit=True)

    def add_user(self, id: int, phone: str = None):
        sql = 'INSERT INTO Users(id, phone) VALUES(?, ?)'
        parameters = (id, phone)
        self.execute(sql, parameters=parameters, commit=True)

    def add_product(self, id: int, name: str, prise: float, numbers: int, photo_path: str):
        sql = 'INSERT INTO Products(id, name, prise, numbers, photo_path) VALUES(?, ?, ?, ?, ?)'
        parameters = (id, name, prise, numbers, photo_path)
        self.execute(sql, parameters, commit=True)

    def select_info(self, table_name: str, **kwargs) -> list:
        sql = f'SELECT * FROM {table_name} WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_all(self, table_name: str) -> list:
        sql = f'SELECT * FROM {table_name}'
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += ' AND '.join([f'{item} = ?' for item in parameters])
        return sql, tuple(parameters.values())

    def update_user_phone(self, id: int, phone: str):
        sql = 'UPDATE Users SET phone=? WHERE id=?'
        return self.execute(sql, parameters=(phone, id), commit=True)

    def update_product_info(self, id: int, column: str, value):
        sql = f'UPDATE Products SET {column}=? WHERE id=?'
        return self.execute(sql, parameters=(value, id), commit=True)

    def get_items_count(self, table_name: str):
        sql = f'SELECT * FROM {table_name}'
        return len(self.execute(sql, fetchall=True))

    def delete_item(self, table_name: str, **kwargs):
        sql = f'DELETE FROM {table_name} WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self, table_name: str):
        self.execute(f'DELETE FROM {table_name} WHERE True', commit=True)

    def drop_all(self, table_name: str):
        self.execute(f'DROP TABLE {table_name}', commit=True)
