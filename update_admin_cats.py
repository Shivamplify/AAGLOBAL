import sqlite3
from bcrypt import hashpw, gensalt

# Database connection
conn = sqlite3.connect('instance/aaglobal.db')

# Add Entertainment and Technology categories, remove Health
# Health has ID 9 based on earlier fetch.
conn.execute("UPDATE articles SET category_id = NULL WHERE category_id = 9")
conn.execute("DELETE FROM categories WHERE id = 9")

# Insert new categories
# We'll use insert ignore or simply insert.
try:
    conn.execute("INSERT INTO categories (name, slug) VALUES ('Entertainment', 'entertainment')")
except sqlite3.IntegrityError:
    pass

try:
    conn.execute("INSERT INTO categories (name, slug) VALUES ('Technology', 'technology')")
except sqlite3.IntegrityError:
    pass

# Update admin credentials
pw_hash = hashpw("#Shivam2002".encode(), gensalt(rounds=12)).decode()
conn.execute("UPDATE admins SET email = 'Shivamext', password_hash = ? WHERE id = 1", (pw_hash,))

conn.commit()
conn.close()
print("DB updated successfully!")