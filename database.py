import sqlite3
from parse import get_number_from_site, get_amountprice_from_site


conn = sqlite3.connect('data.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS cards(number varchar, amount varchar );
""")
conn.commit()

get_data1 = get_number_from_site(100)
get_data2 = get_amountprice_from_site(100)
get_data3 = zip(get_data1, get_data2)

for i, j in get_data3:
    cur.execute("INSERT INTO cards(number, amount) VALUES(?,?)", (i, j))

conn.commit()
conn.close()













