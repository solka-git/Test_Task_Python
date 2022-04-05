import csv
from pymongo import MongoClient

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


db = MongoClient().test_task_db
csv_reader = read_csv(file_name)

for iter in csv_reader:
    db.csv_data.insert_one(dict(zip(['col1', 'col2', 'col3', 'col4', 'col5', 'col6'], iter)))

db.csv_data.delete_many({"col3": {"$regex": r'^\D.*'}})
