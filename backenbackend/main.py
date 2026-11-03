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
