import sqlite3

connection = sqlite3.connect('telegram.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_title ON Products (title)")



def get_all_products():
    cursor.execute("SELECT * FROM Products")
    products_list = cursor.fetchall()
    connection.commit()
    connection.close()
    return products_list



# initiate_db()
#
#
#
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#                    (f'Продукт {i}', f'Описание {i}', i*100))



connection.commit()
# connection.close()
