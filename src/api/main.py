# main.py
import json
from fastapi import FastAPI
import os
from sqlalchemy import create_engine, text

print(os.environ['DB_URL'])

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/jobs")
async def jobs():
    conn_string = os.environ.get("DB_URL")
    engine = create_engine(conn_string)
    with engine.connect() as conn:
        sql=text("SELECT occ_code, occ_title, a_mean::float, tot_emp FROM jobs WHERE a_mean > 100000 ORDER BY a_mean;")
        result = conn.execute(sql)
    joblist = [list(row) for row in result]
    return json.dumps(joblist)

@app.get("/jobs/{job_id}")
async def job(job_id):
    conn_string = os.environ.get("DB_URL")
    engine = create_engine(conn_string)
    with engine.connect() as conn:
        sql=text(f"SELECT occ_code, occ_title, a_mean::float, tot_emp FROM jobs WHERE occ_code = '{job_id}';")
        result = conn.execute(sql)
    joblist = [list(row) for row in result]
    return json.dumps(joblist)