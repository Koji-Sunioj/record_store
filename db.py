import os
import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")

def get_db_connection():
    conn = psycopg2.connect(host=config["HOST"],
    database=config["DATABASE"], 
    user=config["USER"],
    password=config["PASSWORD"])
    return conn

def to_dict(cursor,values):
    columns = [desc[0] for desc in cursor.description]
    return dict((column,value) for column, value in zip(columns,values))

def table_scan(args=None):
    print(config["DATABASE"])
    conn = get_db_connection()
    cur = conn.cursor()
    query = "select album_id, artist, title, price, release_date,stock from albums order by album_id asc;"
    cur.execute(query)
    values = cur.fetchall()
    tobereturned = []
    for row in values:
        new_dict = to_dict(cur,row)
        tobereturned.append(new_dict)
    cur.close()
    conn.close()
    return tobereturned

def create_album(values):
    conn = get_db_connection()
    cur = conn.cursor()
    command = "insert into  albums (artist, title, release_date, stock, price) VALUES(%s, %s, %s, %s, %s) returning *;"
    cur.execute(command,(values["artist"],values["title"],values["release_date"],values["stock"],values["price"]))
    created = to_dict(cur,cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    return created

def patch_album(album_id, values):
    conn = get_db_connection()
    cur = conn.cursor()
    command = "update albums set artist=%s, title=%s,release_date=%s,stock=%s,price=%s where album_id=%s returning *;"
    cur.execute(command,(values["artist"],values["title"],values["release_date"],values["stock"],values["price"],str(album_id)))
    updated = to_dict(cur,cur.fetchone())
    conn.commit()
    cur.close()
    conn.close()
    return updated

def get_album(album_id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "select album_id, artist, title, price, release_date,stock from albums where album_id=%s;"
    cur.execute(query,(str(album_id),))
    album = to_dict(cur,cur.fetchone())
    cur.close()
    conn.close()
    return album

def delete_album(album_id):
    conn = get_db_connection()
    cur = conn.cursor()
    command = "delete from albums where album_id=%s;"
    cur.execute(command,(str(album_id),))
    conn.commit()
    cur.close()
    conn.close()




