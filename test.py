import pyodbc

# server = '192.168.100.188:1433'
# user = "sa"
# password = "jack123"
# database = "jack"
# conn = pymssql.connect(server, user, password, database)

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.100.189,1433;DATABASE=jack;UID=sa;PWD=jack123')

if conn:
    print("成功")
conn.close()
