from fastapi import FastAPI

app = FastAPI()

usuarios = [
    {
        "id": 1,
        "nome": "Maristela Costa",
        "cargo": "Administrador"
    }
]

ativos = [
    {
        "id": 1,
        "nome": "Notebook Dell",
        "categoria": "Hardware",
        "status": "Ativo"
    }
]


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
    return usuarios


@app.get("/ativos")
def listar_ativos():
    return ativos


@app.post("/usuarios")
def criar_usuario(usuario: dict):
    usuarios.append(usuario)
    return {
        "mensagem": "Usuário criado",
        "dados": usuario
    }


@app.post("/ativos")
def criar_ativo(ativo: dict):
    ativos.append(ativo)
    return {
        "mensagem": "Ativo criado",
        "dados": ativo
    }
@app.get("/dashboard")
def dashboard():
    return {
        "usuarios": 2,
        "ativos": 2,
        "status": "operacional",
        "versao": "1.0"
    }
