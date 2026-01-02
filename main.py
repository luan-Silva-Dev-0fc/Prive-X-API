import os
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

app = FastAPI(title="X-PRIVE API", description="API para gerenciamento de sites/atalhos")

# CORS confiável
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode restringir para seu front-end real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SiteSchema(BaseModel):
    name: str
    url: str

def get_connection():
    try:
        return psycopg2.connect(DB_URL)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar no banco: {e}")

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
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name, url FROM sites ORDER BY id DESC;")
        dados = cur.fetchall()
        cur.close()
        conn.close()
        return [{"id": s[0], "name": s[1], "url": s[2]} for s in dados]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar sites: {e}")

@app.post("/sites")
def post_site(site: SiteSchema):
    try:
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar site: {e}")

@app.delete("/sites/{id_site}")
def delete_site(id_site: int):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM sites WHERE id = %s RETURNING id;", (id_site,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if deleted:
            return {"status": "removido", "id": deleted[0]}
        else:
            raise HTTPException(status_code=404, detail="Site não encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar site: {e}")
