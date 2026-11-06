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


@app.get("/status")
def status():
    return {
        "status": "online"
    }


@app.get("/usuarios")
def listar_usuarios():
    return [
        {
            "id": 1,
            "nome": "Maristela Costa",
            "cargo": "Administrador"
        },
        {
            "id": 2,
            "nome": "Usuário Teste",
            "cargo": "Analista"
        }
    ]


@app.get("/ativos")
def listar_ativos():
    return [
        {
            "id": 1,
            "nome": "Notebook Dell",
            "categoria": "Hardware",
            "status": "Ativo"
        },
        {
            "id": 2,
            "nome": "Monitor LG",
            "categoria": "Periférico",
            "status": "Ativo"
        }
    ]


@app.get("/info")
def info():
    return {
        "nome": "SmartBI IA",
        "versao": "1.0.0",
        "status": "Em desenvolvimento"
    }
