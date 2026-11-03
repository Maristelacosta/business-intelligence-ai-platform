from fastapi import FastAPI

app = FastAPI()

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
