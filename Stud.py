import sqlite3 as sql


def connect():
    return sql.connect('db.sqlite3')


def process(query):
    try:
        db=connect()
        db.execute(query)
        db.commit()
        return 'table created'
    except Exception as e:
        print(e)


def create_table():
    query="CREATE TABLE info(id integer primary key ,name text,mobile integer unique,year integer,batchcode text)"
    process(query)


def insert_data(id,name,mobile_no,year,batchcode):
    query=f"insert into info values({id},'{name}',{mobile_no},{year},'{batchcode}')"
    process(query)
    return 'data added to the data base'


def Show():
    query="select * from info"
    try:
        db=connect()
        result = db.execute(query)
        data = result.fetchall()  # fetches the data
        return data
    except Exception as e:
        print(e)


def delete(id):
    query = f'''DELETE from info where id={id};'''
    process(query)


def fetch_user(id):
    query = f'select * from info where id={id}'
    try:
        db=connect()
        result = db.execute(query)
        return result.fetchall()[0]

    except Exception as e:
        print(e)


def update_by_id(id,name,mobile_no,year,batchcode):
    query=f'''update info set name='{name}',mobile={mobile_no},year={year},batchcode='{batchcode}' 
    where id={id};'''
    try:
        db=connect()
        db.execute(query)
        db.commit()
        return 'done'
    except Exception as e:
        print(e)



