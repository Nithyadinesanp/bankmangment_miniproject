import sqlite3
con=sqlite3.connect("bank.db")
cur=con.cursor()
#Admin table
cur.execute("""CREATE TABLE IF NOT EXISTS admin(admin_id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE NOT NULL,password TEXT NOT NULL)""")
#customer table
cur.execute("""CREATE TABLE IF NOT EXISTS customer(customer_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,phone TEXT,address TEXT)""")
#account table
cur.execute("""CREATE TABLE IF NOT EXISTS account(account_no INTEGER PRIMARY KEY,customer_id INTEGER,account_type TEXT,balance REAL DEFAULT 0,FOREIGN KEY(customer_id)REFERENCES customer(customer_id))""")
#user login table
cur.execute("""CREATE TABLE IF NOT EXISTS user_login(user_id INTEGER PRIMARY KEY AUTOINCREMENT,account_no INTGER UNIQUE,user_name TEXT UNIQUE,pass_word TEXT,FOREIGN KEY(account_no)REFERENCES account(account_no))""")
#tracation table
cur.execute("""CREATE TABLE IF NOT EXISTS transactions(transactions_id iNTEGER PRIMARY KEY AUTOINCREMENT,account_no INTEGER,transactions_type TEXT,amount REAL,transactions_date TEXT DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY(account_no)REFERENCES account(account_no))""")
#insert Admin
cur.execute("""INSERT OR IGNORE INTO admin(username,password)VALUES('admin','admin123')""")
con.commit()
con.close()
print("All the table createrd successfully ")