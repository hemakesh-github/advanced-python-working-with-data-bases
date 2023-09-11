#TO DO:
#create, insert, query
#data for tech company's sales
#columms : order_num, order_type, cust_name, prod_category, prod_number, prod_name, quantity, price, discount, and order total

#create database Red30
#table called sales
#5 rows, order_num is primary key
#query for most expensive order
#discover who ordered the most expensive order


from sqlalchemy import Column, String, Float, Integer, create_engine, ForeignKey, select
from sqlalchemy.orm import registry,relationship, Session

engine = create_engine('mysql+mysqlconnector://root:hemakesh%40mysql@localhost:3306/Red30',
                       echo = True)

mapper_registry = registry()

Base = mapper_registry.generate_base()
class Sales(Base):
    __tablename__ = "sales"
    order_num = Column(Integer, primary_key = True)
    order_type = Column(String(length = 20))
    cust_name = Column(String(length=20))
    prod_category = Column(String(length = 150))
    prod_number = Column(String(length = 10))
    prod_name = Column(String(length = 200))
    quantity = Column(Integer)
    price = Column(Float)
    discount = Column(Float)
    order_total = Column(Float)

    def __repr__(self):
        return "<Sales(oder_num = '{0}', order_type = '{1}', cust_name = '{2}', prod_category = '{3}',prod_number = '{4}', prod_name = '{5}', quantity = '{6}', price = '{7}', discount = '{8}', order_total = '{9}')".format(
            self.order_num, self.order_type, self.cust_name, self.prod_category, self.prod_number, self.prod_name, self.quantity, self.price, self.discount, self.order_total
        )
    
Base.metadata.create_all(engine)

with Session(engine) as session:
    sale1 = Sales(order_num=1100935, order_type = "online", cust_name="Spencer Educators", prod_category = "education", prod_number="DK204",
		prod_name="BYOD-300", quantity=2, price=89, discount=0, order_total=178)
    
    sale2 = Sales(order_num=1100948, order_type = "online", cust_name="Ewan Ladd",prod_category = "education", prod_number="TV810",
		prod_name="Understanding Automation", quantity=1, price=44.95, discount=0, order_total=44.95)
    
    sale3 = Sales(order_num=1100963, order_type = "online", cust_name="Stehr Group",prod_category = "education", prod_number="DS301",
		prod_name="DA-SA702 Drone", quantity=3, price=399, discount=.1, order_total=1077.3)
    
    sale4 = Sales(order_num=1100971, order_type = "online", cust_name="Hettinger and Sons",prod_category = "education", prod_number="DS306",
		prod_name="DA-SA702 Drone", quantity=12, price=250, discount=.5, order_total=1500)

    sale5 = Sales(order_num=1100998, order_type = "online", cust_name="Luz O'Donoghue",prod_category = "education", prod_number="TV809",
		prod_name="Understanding 3D Printing", quantity=1, price=42.99, discount=0, order_total=42.99)
    
    sales = [sale1, sale2, sale3, sale4, sale5]
    session.flush()
    session.bulk_save_objects(sales)
    session.commit()

with Session(engine) as session:
    smt = select(Sales).order_by(Sales.order_total.desc()).limit(1)

    results = (session.execute(smt))
    result = (results.scalar()) 
    print(result)