import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///hi.db', echo = True)

with engine.connect() as conn:
    result = conn.execute(sqlalchemy.text("SELECT * FROM hi"))
    for row in result:
         print(row)

# metadata = sqlalchemy.metadata()

# movies_table = sqlalchemy.Table("hi",metadata,
#                                 sqlalchemy.Column('name', sqlalchemy.Text),
#                                 sqlalchemy.Column('msg', sqlalchemy.Text))

# metadata.create_all(engine)

# with engine.connect() as conn:
