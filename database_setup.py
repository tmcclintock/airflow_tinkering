"""
A very short script to set up the sql database
with the correct permissions for Airflow.
"""
import sqlite3

basename = "airflow"
name = f"{basename}.db"

conn = sqlite3.connect(name)
c = conn.cursor()

#c.execute("CHARACTER SET utf8 COLLATE utf8_unicode_ci;")
#c.execute("GRANT ALL PRIVILEGES ON {basename}. To 'airflow'@'localhost'")
#c.exectue("FLUSH PRIVILEGES")
#conn.commit()
conn.close()
