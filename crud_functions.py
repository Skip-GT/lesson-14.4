import sqlite3


def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


"""def populate_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    products = [
        ('Витамин А', 'для зрения, роста, деления клеток и иммунитета.', 100),
        ('Витамин С', 'укрепляет десны, зубы и сосуды.', 200),
        ('Витамин D3', 'регулирует обмен кальция и фосфора.', 300),
        ('Витамин B', 'для обмена веществ и функционирования нервной системы.', 400)
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    conn.commit()
    conn.close()"""