from fastapi import FastAPI

app = FastAPI(
    title="SmartBI IA",
    description="Plataforma de Business Intelligence com Inteligência Artificial",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "mensagem": "Bem-vindo à IA SmartBI"
    }
