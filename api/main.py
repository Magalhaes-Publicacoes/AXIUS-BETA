from datetime import datetime

from fastapi import FastAPI

app = FastAPI(
    title="ÁXIUS API",
    description="API do Ecossistema Jurídico ÁXIUS",
    version="0.1.0",
)


@app.get("/")
def inicio():
    return {
        "produto": "ÁXIUS",
        "descricao": "Ecossistema Jurídico",
        "status": "ONLINE",
        "versao": "0.1.0",
        "horario": datetime.now().isoformat(),
    }


@app.get("/health")
def health():
    return {
        "status": "ONLINE",
        "servico": "AXIUS API",
    }
