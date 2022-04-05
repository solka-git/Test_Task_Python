import pymysql
import csv

from config import host, user, db_name

file_name = 'result_task_A.csv'


def read_csv(file_name):
    with open(file_name) as src:
        csv_reader = csv.reader(src)
        read_new = []
        for i in list(csv_reader):
            row_new = []
            for item in str(i).split(' '):
                item_new = item.replace("[", "").replace("]", "").replace("\'", "")
                if item_new != '':
                    row_new.append(item_new)
            read_new.append(row_new)
        return read_new


with pymysql.connect(host=host, user=user) as conn:
    with conn.cursor() as cur:
        cur.execute(f"""create database if not exists {db_name}""")
    conn.commit()

with pymysql.connect(host=host, user=user, database=db_name) as conn:
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f"""create table if not exists data(
                               col1 varchar(8),
                               col2 varchar(8),
                               col3 varchar(8),
                               col4 varchar(8),
                               col5 varchar(8),
                               col6 varchar(8));""")
        reader = read_csv(file_name)

        for iter in reader:
            query = "insert into data (col1, col2, col3, col4, col5, col6) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.executemany(query, list(map(tuple, list(iter))))
            cur.execute(query)

        cur.execute("DELETE FROM data WHERE LEFT(col2, 1) REGEXP '^[0-9]+$';")
