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
        sql=text("SELECT occ_title, a_mean, tot_emp FROM jobs WHERE a_mean > 100000 ORDER BY a_mean;")
        result = conn.execute(sql)
    joblist = [row.items() for row in result]
    breakpoint()
    return json.dumps(joblist)
    return joblist

# @app.get("/jobs/{job_id}")
# async def job(job_id):
#     job_id = int(job_id)
#     if job_id >= 0 and job_id < len(joblist):
#         return joblist[job_id]
#     else:
#         return "error"