# main.py

from fastapi import FastAPI
import os

print(os.environ['DB_URL'])

app = FastAPI()

joblist=["Nurse", "Teacher", "Firefighter", "Police Officer", "Backend Worker"]

print (len(joblist))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/jobs")
async def jobs():
    return joblist

@app.get("/jobs/{job_id}")
async def job(job_id):
    job_id = int(job_id)
    if job_id >= 0 and job_id < len(joblist):
        return joblist[job_id]
    else:
        return "error"