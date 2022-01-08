import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import Connection

db_connection : Connection = None

def create_connection(db_file):
    """ 
        Create a database connection to a database that resides in the local folder
    """
    conn = None;
    try:
        conn = sqlite3.connect(db_file)

    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ 
        Create a table from the create_table_sql statement

        :param 
            conn : Connection object
            create_table_sql : a CREATE TABLE statement

        :return
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_seller(conn, seller):
    """
        Create a new seller into the seller table

        :param 
            conn :
            seller :

        :return
            seller id
    """
    sql = ''' INSERT OR IGNORE INTO seller(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, [seller])
    conn.commit()
    return cur.lastrowid

def create_sale_item(conn, seller_id, customer_name, sale_date, sale_item_name, sale_value):
    """
        Create a new seller into the seller table

        :param 
            conn :
            seller :

        :return
            seller id
    """
    sql = '''
        INSERT INTO sale_item(
            id_seller, 
            customer_name, 
            sale_date,
            sale_item_name,
            sale_value
        ) 
        VALUES(?,?,?,?,?)
    '''
    cur = conn.cursor()
    cur.execute(sql, (seller_id, customer_name, sale_date, sale_item_name, sale_value))
    conn.commit()
    return cur.lastrowid


def config_database():
    database = r".\sellersrank.db"

    sql_create_sellers_table = """ CREATE TABLE IF NOT EXISTS seller (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL UNIQUE
                                ); """

    sql_create_sales_items_table = """ CREATE TABLE IF NOT EXISTS sale_item (
                                        id INTEGER PRIMARY KEY,
                                        id_seller INTEGER NOT NULL,
                                        customer_name TEXT NOT NULL,
                                        sale_date DATE NOT NULL,
                                        sale_item_name TEXT NOT NULL,
                                        sale_value FLOAT NOT NULL,
                                        FOREIGN KEY (id_seller) REFERENCES seller (id)
                                    ); """

    # create a database connection
    db_connection = create_connection(database)

    # create tables
    if db_connection is not None:
        # create projects table
        create_table(db_connection, sql_create_sellers_table)

        # create tasks table
        create_table(db_connection, sql_create_sales_items_table)

        with db_connection:
            # create a new project
            seller = ('Nike');
            create_seller(db_connection, seller)

            seller = ('Adidas');
            create_seller(db_connection, seller)

            seller = ('Puma');
            create_seller(db_connection, seller)
            
            seller = ('Umbro');
            create_seller(db_connection, seller)

            seller = ('Fila');
            create_seller(db_connection, seller)

    else:
        print("Error! cannot create the database connection.")

def get_connection():
    database = r".\sellersrank.db"

    db_connection = create_connection(database)

    return db_connection