import psycopg2
import pandas as pd
from sqlalchemy import create_engine, text
import os

conn_string = os.environ.get("DB_URL")

engine = create_engine(conn_string)
with engine.connect() as conn:
    sql=text("SELECT occ_title, a_mean, tot_emp FROM jobs WHERE a_mean > 100000 ORDER BY a_mean;")
    result = conn.execute(sql)
    for row in result:
        print(row)
