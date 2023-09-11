import psycopg2

def insert_sale(cur, order_num, cust_name, prod_num):
   
    sales_data = {"order_num" : order_num,
                  'cust_name' : cust_name,
                  'product_number': prod_num}
    
    cur.execute("INSERT INTO sales VALUES (%(order_num)s, %(cust_name)s, %(product_number)s)", sales_data)

conn = psycopg2.connect(database = "red30",
                        user = "postgres",
                        password = "hemakesh",
                        host = "localhost",
                        port = "5432")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS SALES(ORDER_NUM INT PRIMARY KEY, CUST_NAME TEXT,PROD_NUMBER TEXT)")



order_num = int(input('order Num: '))
cust_name = input("cust name")
prod_number = input("prod num: ")
insert_sale(cursor,order_num, cust_name, prod_number)

conn.commit()
conn.close()