import psycopg2


conn = psycopg2.connect(database = "red30",
                        user = "postgres",
                        password = "hemakesh",
                        host = "localhost",
                        port = "5432")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS SALES(ORDER_NUM INT PRIMARY KEY, CUST_NAME TEXT,PROD_NUMBER TEXT)")

sales = [(1, "hello", "3a"),(2, "hi", "3b")]

cursor.executemany("INSERT INTO sales VALUES (%s, %s, %s)", sales)

conn.commit()
conn.close()