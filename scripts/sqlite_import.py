import os
import json
import sqlite3

connection = sqlite3.connect('data/sqlite3/mnist-training-data.db')
cursor = connection.cursor()

tables = cursor.execute("SELECT name FROM sqlite_master").fetchone()

from datasets import load_dataset
mnist = load_dataset("mnist")

def create_table(cursor):
  table_sql = """
  CREATE TABLE mnist_training_data (
    id INTEGER PRIMARY KEY, 
    image_num TEXT,
    true_label TEXT,
    true_pred REAL,
    pred_0 REAL,
    pred_1 REAL,
    pred_2 REAL, 
    pred_3 REAL, 
    pred_4 REAL, 
    pred_5 REAL, 
    pred_6 REAL, 
    pred_7 REAL,
    pred_8 REAL,
    pred_9 REAL
  )
  """
  cursor.execute(table_sql)

print('tables', tables)
if 'mnist_training_data' not in tables:
  create_table(cursor)

def insert_row(cursor, row):
  values = ', '.join(row)
  insert_sql = f"INSERT INTO mnist_training_data VALUES ({values})"
  cursor.execute(insert_sql)

def true_label_for(index):
  assert type(index) == int
  return mnist['train'][index]['label']

def read_files(data_dir='data/classify_mnist/'):
  filenames = os.listdir(data_dir)
  #filenames = ['start_34500_end_34599.json']
  rows = []
  for filename in filenames:
    with open(data_dir + filename, 'r') as f:
      data = json.loads(f.read())
      rows = []
      for key in data.keys():
        index = int(key)
        true_label = true_label_for(index)
        true_index = int(true_label)
        preds = data[key]
        true_pred = preds[true_index]  
        row_prefix = [index, str(index), true_label, true_pred]
        row = tuple(row_prefix + preds)
        #print('while reading file', filename)
        #print('got row', row)
        rows.append(row)
      
      qs = ', '.join(['?'] * 14)
      sql = f"INSERT INTO mnist_training_data VALUES ({qs})"
      try:
        cursor.executemany(sql, rows)
        connection.commit()
      except sqlite3.IntegrityError as error:
        print('error', error)
        print('Could not perform insert')
  
  #return rows

read_files()