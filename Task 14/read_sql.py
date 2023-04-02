import pandas as pd
import sqlite3

query = """
 CREATE TABLE test
 (a VARCHAR(20), b VARCHAR(20),
 c REAL, d INTEGER );
 """

con = sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()

data = [ ('Atlanta', 'alabama', 1.23, 6),
         ('Tennesse', 'mississipi', 7, 21),
         ('california', 'ohio', 1.7, 5)]

stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)

con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()
print(rows)     # will display data tuple
print(cursor.description)

# displaying in dataframe
# via for loop column wise parsing
print(pd.DataFrame(rows, columns=[x[0] for x in cursor.description]))
