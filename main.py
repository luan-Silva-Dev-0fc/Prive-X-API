import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SiteSchema(BaseModel):
    name: str
    url: str

def get_connection():
    return psycopg2.connect(DB_URL)


@app.on_event("startup")
def setup_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sites (
            id SERIAL PRIMARY KEY, 
            name TEXT NOT NULL, 
            url TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.get("/sites")
def get_sites():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, url FROM sites ORDER BY id DESC;")
    dados = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": s[0], "name": s[1], "url": s[2]} for s in dados]


@app.post("/sites")
def post_site(site: SiteSchema):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sites (name, url) VALUES (%s, %s) RETURNING id, name, url;", 
        (site.name, site.url)
    )
    novo_site = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return {"id": novo_site[0], "name": novo_site[1], "url": novo_site[2]}


@app.delete("/sites/{id_site}")
def delete_site(id_site: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM sites WHERE id = %s;", (id_site,))
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "removido", "id": id_site}