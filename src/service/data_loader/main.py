import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os

conn_string = os.environ.get("DB_URL")

db = create_engine(conn_string)
conn = db.connect()

df = pd.read_excel('tmp/national_M2021_dl.xlsx')

print(df)
print(type(df.columns))

new_columns=[]

for column in df.columns:
    x=column.lower()
    new_columns.append(x)

print(new_columns)

df.columns = new_columns

df.to_sql('jobs', con=conn, if_exists='append', index=False)

# data = {'Name': ['Tom', 'dick', 'harry'],
#         'Age': [22, 21, 24]}

# print (type(data))
# print (data.keys())
# print (data.values())

# df2 = pd.DataFrame(data)

# print (df2)

# data = {'Name': ['Tom', 'dick', 'harry'],
#         'Age': [22, 21, 24]}

# df2.to_sql('data')

# print(df)