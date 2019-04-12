import sqlite3

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS store(item_name TEXT,quantity INTEGER,price REAL)")
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item,quantity,price))
    conn.commit()
    conn.close()
def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

def update(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    print("updating...")
    cur.execute("UPDATE store SET quantity=?,price=? where item_name=?",(quantity,price,item))
    conn.commit()
    conn.close()

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    print("deleting...")
    cur.execute("DELETE FROM store WHERE item_name=?", (item,))
    conn.commit()
    conn.close()

print(view())
delete("Wine Glass")
print(view())
