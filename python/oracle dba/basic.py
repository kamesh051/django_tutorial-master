import cx_Oracle
con = cx_Oracle.connect('scott','tiger','localhost:1521/orcl')
cur = con.cursor()
cur.execute("select * from emp")
for row in cur:
    print(row)
cur.close()
con.close()
