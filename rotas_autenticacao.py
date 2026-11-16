from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["autenticacao"])

@auth_router.get("/")
async def autenticacao():
    return {"mensagem": "Voce acessou a rota de autenticação", "autenticado": False}
