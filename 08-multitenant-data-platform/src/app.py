from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3

app=FastAPI(title="Multi-Tenant Data Platform")
db=sqlite3.connect("tenants.db",check_same_thread=False)
db.execute("create table if not exists events(tenant_id text, event_id text, payload text)")
db.commit()

class Event(BaseModel):
    event_id:str
    payload:dict

@app.post("/events")
def ingest(event:Event, x_tenant_id:str=Header(...)):
    if not x_tenant_id.strip():
        raise HTTPException(400,"tenant_id obrigatório")
    db.execute("insert into events values(?,?,?)",(x_tenant_id,event.event_id,str(event.payload)))
    db.commit()
    return {"tenant_id":x_tenant_id,"status":"accepted"}
