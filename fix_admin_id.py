import sqlite3
conn = sqlite3.connect('instance/aaglobal.db')
conn.execute("UPDATE admins SET email = 'shivamext' WHERE id = 1")
conn.commit()
conn.close()