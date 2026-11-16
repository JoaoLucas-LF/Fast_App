from fastapi import FastAPI

app = FastAPI()

from rotas_autenticacao import auth_router
from rotas_ordem import order_router

app.include_router(auth_router)
app.include_router(order_router)


"""
Rodar codigo, execute no terminal = uvicorn main:app --reload

Para criar uma rota, é necessário definir:
- endpoint:
 / ordens
Tipo de requisição que irá ser associado a ela

Rest APIs
Get -> Leitura/pegar
Post -> Enviar/Criar
Put/Patch -> editar/atualizar
Delete -> deletar/excluir
"""

